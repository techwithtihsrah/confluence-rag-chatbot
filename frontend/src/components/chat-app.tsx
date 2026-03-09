// "use client";

// import { useEffect, useMemo, useState } from "react";
// import {
//   ChatResponse,
//   SessionDetailResponse,
//   SessionSummary,
//   createSession,
//   getSessionDetail,
//   getSessions,
//   sendChatMessage,
// } from "@/lib/api";

// type DisplayMessage = {
//   id: string;
//   role: "user" | "assistant";
//   content: string;
//   createdAt?: string;
//   sources?: ChatResponse["sources"];
// };

// export default function ChatApp() {
//   const [sessions, setSessions] = useState<SessionSummary[]>([]);
//   const [selectedSessionId, setSelectedSessionId] = useState<string | null>(
//     null,
//   );
//   const [messages, setMessages] = useState<DisplayMessage[]>([]);
//   const [input, setInput] = useState("");
//   const [isLoadingSessions, setIsLoadingSessions] = useState(true);
//   const [isSending, setIsSending] = useState(false);
//   const [error, setError] = useState("");

//   const selectedSession = useMemo(
//     () => sessions.find((session) => session.id === selectedSessionId) || null,
//     [sessions, selectedSessionId],
//   );

//   async function loadSessions(keepCurrentSelection = true) {
//     try {
//       const data = await getSessions();
//       setSessions(data.sessions);

//       if (!keepCurrentSelection) {
//         return;
//       }

//       if (!selectedSessionId && data.sessions.length > 0) {
//         setSelectedSessionId(data.sessions[0].id);
//       }
//     } catch (err) {
//       setError("Failed to load sessions.");
//     } finally {
//       setIsLoadingSessions(false);
//     }
//   }

//   async function loadSessionMessages(sessionId: string) {
//     try {
//       const detail: SessionDetailResponse = await getSessionDetail(sessionId);

//       const normalizedMessages: DisplayMessage[] = detail.messages.map(
//         (message) => ({
//           id: String(message.id),
//           role: message.role,
//           content: message.content,
//           createdAt: message.created_at,
//         }),
//       );

//       setMessages(normalizedMessages);
//     } catch (err) {
//       setError("Failed to load session messages.");
//     }
//   }

//   async function handleCreateNewChat() {
//     setError("");

//     try {
//       const session = await createSession();
//       await loadSessions(false);
//       const refreshed = await getSessions();
//       setSessions(refreshed.sessions);
//       setSelectedSessionId(session.id);
//       setMessages([]);
//     } catch (err) {
//       setError("Failed to create a new chat.");
//     }
//   }

//   async function handleSelectSession(sessionId: string) {
//     setSelectedSessionId(sessionId);
//     await loadSessionMessages(sessionId);
//   }

//   async function handleSendMessage() {
//     const trimmed = input.trim();

//     if (!trimmed || isSending) {
//       return;
//     }

//     setError("");
//     setIsSending(true);

//     try {
//       let currentSessionId = selectedSessionId;

//       if (!currentSessionId) {
//         const newSession = await createSession();
//         currentSessionId = newSession.id;
//         setSelectedSessionId(newSession.id);
//       }

//       await sendChatMessage({
//         message: trimmed,
//         sessionId: currentSessionId ?? undefined,
//         k: 4,
//       });

//       setInput("");

//       if (currentSessionId) {
//         await loadSessionMessages(currentSessionId);
//       }

//       await loadSessions(false);
//       const refreshed = await getSessions();
//       setSessions(refreshed.sessions);
//     } catch (err) {
//       setError("Failed to send message.");
//     } finally {
//       setIsSending(false);
//     }
//   }

//   useEffect(() => {
//     loadSessions();
//   }, []);

//   useEffect(() => {
//     if (selectedSessionId) {
//       loadSessionMessages(selectedSessionId);
//     }
//   }, [selectedSessionId]);

//   return (
//     <div className="app-shell">
//       <aside className="sidebar">
//         <div className="sidebar-header">
//           <div>
//             <h1 className="sidebar-title">Confluence RAG Chatbot</h1>
//             <p className="sidebar-subtitle">Sessions</p>
//           </div>
//           <button className="primary-button" onClick={handleCreateNewChat}>
//             New Chat
//           </button>
//         </div>

//         <div className="session-list">
//           {isLoadingSessions ? (
//             <div className="empty-state">Loading sessions...</div>
//           ) : sessions.length === 0 ? (
//             <div className="empty-state">No saved sessions yet.</div>
//           ) : (
//             sessions.map((session) => (
//               <button
//                 key={session.id}
//                 className={
//                   session.id === selectedSessionId
//                     ? "session-item session-item-active"
//                     : "session-item"
//                 }
//                 onClick={() => handleSelectSession(session.id)}
//               >
//                 <div className="session-title">{session.title}</div>
//                 <div className="session-time">
//                   {new Date(session.updated_at).toLocaleString()}
//                 </div>
//               </button>
//             ))
//           )}
//         </div>
//       </aside>

//       <main className="chat-panel">
//         <div className="chat-header">
//           <div>
//             <h2 className="chat-title">
//               {selectedSession ? selectedSession.title : "New conversation"}
//             </h2>
//             <p className="chat-subtitle">
//               Ask questions grounded in your Confluence knowledge base.
//             </p>
//           </div>
//         </div>

//         <div className="messages-area">
//           {messages.length === 0 ? (
//             <div className="welcome-card">
//               <h3>Start chatting</h3>
//               <p>
//                 Ask something like:
//                 <br />
//                 “How do I set up Python for the banking chatbot environment?”
//               </p>
//             </div>
//           ) : (
//             messages.map((message) => (
//               <div
//                 key={message.id}
//                 className={
//                   message.role === "user"
//                     ? "message-row message-row-user"
//                     : "message-row message-row-assistant"
//                 }
//               >
//                 <div
//                   className={
//                     message.role === "user"
//                       ? "message-bubble message-bubble-user"
//                       : "message-bubble message-bubble-assistant"
//                   }
//                 >
//                   <div className="message-role">
//                     {message.role === "user" ? "You" : "Assistant"}
//                   </div>
//                   <div className="message-content">{message.content}</div>

//                   {message.role === "assistant" &&
//                     message.sources &&
//                     message.sources.length > 0 && (
//                       <div className="sources-block">
//                         <div className="sources-title">Sources</div>
//                         <ul className="sources-list">
//                           {message.sources.map((source) => (
//                             <li key={`${source.page_id}-${source.source_url}`}>
//                               <a
//                                 href={source.source_url}
//                                 target="_blank"
//                                 rel="noreferrer"
//                               >
//                                 {source.page_title}
//                               </a>
//                             </li>
//                           ))}
//                         </ul>
//                       </div>
//                     )}
//                 </div>
//               </div>
//             ))
//           )}
//         </div>

//         {error ? <div className="error-banner">{error}</div> : null}

//         <div className="composer">
//           <textarea
//             className="composer-input"
//             placeholder="Ask a question about your Confluence docs..."
//             value={input}
//             onChange={(e) => setInput(e.target.value)}
//             rows={3}
//           />
//           <button
//             className="primary-button composer-button"
//             onClick={handleSendMessage}
//             disabled={isSending}
//           >
//             {isSending ? "Sending..." : "Send"}
//           </button>
//         </div>
//       </main>
//     </div>
//   );
// }

// "use client";

// import { useEffect, useMemo, useState } from "react";
// import {
//   ChatResponse,
//   SessionDetailResponse,
//   SessionSummary,
//   createSession,
//   getSessionDetail,
//   getSessions,
//   sendChatMessage,
// } from "@/lib/api";

// type DisplayMessage = {
//   id: string;
//   role: "user" | "assistant";
//   content: string;
//   createdAt?: string;
//   sources?: ChatResponse["sources"];
// };

// export default function ChatApp() {
//   const [sessions, setSessions] = useState<SessionSummary[]>([]);
//   const [selectedSessionId, setSelectedSessionId] = useState<string | null>(
//     null,
//   );
//   const [messages, setMessages] = useState<DisplayMessage[]>([]);
//   const [input, setInput] = useState("");
//   const [isLoadingSessions, setIsLoadingSessions] = useState(true);
//   const [isSending, setIsSending] = useState(false);
//   const [error, setError] = useState("");

//   const selectedSession = useMemo(
//     () => sessions.find((session) => session.id === selectedSessionId) || null,
//     [sessions, selectedSessionId],
//   );

//   async function refreshSessions(keepCurrentSelection = true) {
//     const data = await getSessions();
//     setSessions(data.sessions);

//     if (
//       keepCurrentSelection &&
//       !selectedSessionId &&
//       data.sessions.length > 0
//     ) {
//       setSelectedSessionId(data.sessions[0].id);
//     }
//   }

//   async function loadSessions(keepCurrentSelection = true) {
//     try {
//       await refreshSessions(keepCurrentSelection);
//     } catch {
//       setError("Failed to load sessions.");
//     } finally {
//       setIsLoadingSessions(false);
//     }
//   }

//   async function loadSessionMessages(sessionId: string) {
//     try {
//       const detail: SessionDetailResponse = await getSessionDetail(sessionId);

//       const normalizedMessages: DisplayMessage[] = detail.messages.map(
//         (message) => ({
//           id: String(message.id),
//           role: message.role,
//           content: message.content,
//           createdAt: message.created_at,
//           sources: message.sources ?? [],
//         }),
//       );

//       setMessages(normalizedMessages);
//     } catch {
//       setError("Failed to load session messages.");
//     }
//   }

//   async function handleCreateNewChat() {
//     setError("");

//     try {
//       const session = await createSession();
//       await refreshSessions(false);
//       setSelectedSessionId(session.id);
//       setMessages([]);
//     } catch {
//       setError("Failed to create a new chat.");
//     }
//   }

//   async function handleSelectSession(sessionId: string) {
//     setSelectedSessionId(sessionId);
//     await loadSessionMessages(sessionId);
//   }

//   async function handleSendMessage() {
//     const trimmed = input.trim();

//     if (!trimmed || isSending) {
//       return;
//     }

//     setError("");
//     setIsSending(true);

//     try {
//       let currentSessionId = selectedSessionId;

//       if (!currentSessionId) {
//         const newSession = await createSession();
//         currentSessionId = newSession.id;
//         setSelectedSessionId(newSession.id);
//       }

//       await sendChatMessage({
//         message: trimmed,
//         sessionId: currentSessionId ?? undefined,
//         k: 4,
//       });

//       setInput("");

//       if (currentSessionId) {
//         await loadSessionMessages(currentSessionId);
//       }

//       await refreshSessions(false);
//     } catch {
//       setError("Failed to send message.");
//     } finally {
//       setIsSending(false);
//     }
//   }

//   useEffect(() => {
//     loadSessions();
//   }, []);

//   useEffect(() => {
//     if (selectedSessionId) {
//       loadSessionMessages(selectedSessionId);
//     }
//   }, [selectedSessionId]);

//   return (
//     <div className="app-shell">
//       <aside className="sidebar">
//         <div className="sidebar-header">
//           <div>
//             <h1 className="sidebar-title">Confluence RAG Chatbot</h1>
//             <p className="sidebar-subtitle">Sessions</p>
//           </div>
//           <button className="primary-button" onClick={handleCreateNewChat}>
//             New Chat
//           </button>
//         </div>

//         <div className="session-list">
//           {isLoadingSessions ? (
//             <div className="empty-state">Loading sessions...</div>
//           ) : sessions.length === 0 ? (
//             <div className="empty-state">No saved sessions yet.</div>
//           ) : (
//             sessions.map((session) => (
//               <button
//                 key={session.id}
//                 className={
//                   session.id === selectedSessionId
//                     ? "session-item session-item-active"
//                     : "session-item"
//                 }
//                 onClick={() => handleSelectSession(session.id)}
//               >
//                 <div className="session-title">{session.title}</div>
//                 <div className="session-time">
//                   {new Date(session.updated_at).toLocaleString()}
//                 </div>
//               </button>
//             ))
//           )}
//         </div>
//       </aside>

//       <main className="chat-panel">
//         <div className="chat-header">
//           <div>
//             <h2 className="chat-title">
//               {selectedSession ? selectedSession.title : "New conversation"}
//             </h2>
//             <p className="chat-subtitle">
//               Ask questions grounded in your Confluence knowledge base.
//             </p>
//           </div>
//         </div>

//         <div className="messages-area">
//           {messages.length === 0 ? (
//             <div className="welcome-card">
//               <h3>Start chatting</h3>
//               <p>
//                 Ask something like:
//                 <br />
//                 “How do I set up Python for the banking chatbot environment?”
//               </p>
//             </div>
//           ) : (
//             messages.map((message) => (
//               <div
//                 key={message.id}
//                 className={
//                   message.role === "user"
//                     ? "message-row message-row-user"
//                     : "message-row message-row-assistant"
//                 }
//               >
//                 <div
//                   className={
//                     message.role === "user"
//                       ? "message-bubble message-bubble-user"
//                       : "message-bubble message-bubble-assistant"
//                   }
//                 >
//                   <div className="message-role">
//                     {message.role === "user" ? "You" : "Assistant"}
//                   </div>
//                   <div className="message-content">{message.content}</div>

//                   {message.role === "assistant" &&
//                     message.sources &&
//                     message.sources.length > 0 && (
//                       <div className="sources-block">
//                         <div className="sources-title">Sources</div>
//                         <ul className="sources-list">
//                           {message.sources.map((source) => (
//                             <li key={`${source.page_id}-${source.source_url}`}>
//                               <a
//                                 href={source.source_url}
//                                 target="_blank"
//                                 rel="noreferrer"
//                               >
//                                 {source.page_title}
//                               </a>
//                             </li>
//                           ))}
//                         </ul>
//                       </div>
//                     )}
//                 </div>
//               </div>
//             ))
//           )}
//         </div>

//         {error ? <div className="error-banner">{error}</div> : null}

//         <div className="composer">
//           <textarea
//             className="composer-input"
//             placeholder="Ask a question about your Confluence docs..."
//             value={input}
//             onChange={(e) => setInput(e.target.value)}
//             rows={3}
//           />
//           <button
//             className="primary-button composer-button"
//             onClick={handleSendMessage}
//             disabled={isSending}
//           >
//             {isSending ? "Sending..." : "Send"}
//           </button>
//         </div>
//       </main>
//     </div>
//   );
// }

// working without delete button
// "use client";

// import { useEffect, useMemo, useState } from "react";
// import {
//   BulkUpsertResponse,
//   ChatResponse,
//   SessionDetailResponse,
//   SessionSummary,
//   createSession,
//   getSessionDetail,
//   getSessions,
//   sendChatMessage,
//   syncAllPages,
// } from "@/lib/api";

// type DisplayMessage = {
//   id: string;
//   role: "user" | "assistant";
//   content: string;
//   createdAt?: string;
//   sources?: ChatResponse["sources"];
// };

// export default function ChatApp() {
//   const [sessions, setSessions] = useState<SessionSummary[]>([]);
//   const [selectedSessionId, setSelectedSessionId] = useState<string | null>(
//     null,
//   );
//   const [messages, setMessages] = useState<DisplayMessage[]>([]);
//   const [input, setInput] = useState("");
//   const [isLoadingSessions, setIsLoadingSessions] = useState(true);
//   const [isSending, setIsSending] = useState(false);
//   const [isSyncing, setIsSyncing] = useState(false);
//   const [error, setError] = useState("");
//   const [syncError, setSyncError] = useState("");
//   const [syncResult, setSyncResult] = useState<BulkUpsertResponse | null>(null);

//   const selectedSession = useMemo(
//     () => sessions.find((session) => session.id === selectedSessionId) || null,
//     [sessions, selectedSessionId],
//   );

//   async function refreshSessions(keepCurrentSelection = true) {
//     const data = await getSessions();
//     setSessions(data.sessions);

//     if (
//       keepCurrentSelection &&
//       !selectedSessionId &&
//       data.sessions.length > 0
//     ) {
//       setSelectedSessionId(data.sessions[0].id);
//     }
//   }

//   async function loadSessions(keepCurrentSelection = true) {
//     try {
//       await refreshSessions(keepCurrentSelection);
//     } catch {
//       setError("Failed to load sessions.");
//     } finally {
//       setIsLoadingSessions(false);
//     }
//   }

//   async function loadSessionMessages(sessionId: string) {
//     try {
//       const detail: SessionDetailResponse = await getSessionDetail(sessionId);

//       const normalizedMessages: DisplayMessage[] = detail.messages.map(
//         (message) => ({
//           id: String(message.id),
//           role: message.role,
//           content: message.content,
//           createdAt: message.created_at,
//           sources: message.sources ?? [],
//         }),
//       );

//       setMessages(normalizedMessages);
//     } catch {
//       setError("Failed to load session messages.");
//     }
//   }

//   async function handleCreateNewChat() {
//     setError("");

//     try {
//       const session = await createSession();
//       await refreshSessions(false);
//       setSelectedSessionId(session.id);
//       setMessages([]);
//     } catch {
//       setError("Failed to create a new chat.");
//     }
//   }

//   async function handleSelectSession(sessionId: string) {
//     setSelectedSessionId(sessionId);
//     await loadSessionMessages(sessionId);
//   }

//   async function handleSendMessage() {
//     const trimmed = input.trim();

//     if (!trimmed || isSending) {
//       return;
//     }

//     setError("");
//     setIsSending(true);

//     try {
//       let currentSessionId = selectedSessionId;

//       if (!currentSessionId) {
//         const newSession = await createSession();
//         currentSessionId = newSession.id;
//         setSelectedSessionId(newSession.id);
//       }

//       await sendChatMessage({
//         message: trimmed,
//         sessionId: currentSessionId ?? undefined,
//         k: 4,
//       });

//       setInput("");

//       if (currentSessionId) {
//         await loadSessionMessages(currentSessionId);
//       }

//       await refreshSessions(false);
//     } catch {
//       setError("Failed to send message.");
//     } finally {
//       setIsSending(false);
//     }
//   }

//   async function handleSyncAllPages() {
//     setSyncError("");
//     setSyncResult(null);
//     setIsSyncing(true);

//     try {
//       const result = await syncAllPages({
//         limit: 25,
//         chunkSize: 800,
//         chunkOverlap: 150,
//       });
//       setSyncResult(result);
//     } catch (err) {
//       setSyncError("Failed to sync Confluence pages.");
//     } finally {
//       setIsSyncing(false);
//     }
//   }

//   useEffect(() => {
//     loadSessions();
//   }, []);

//   useEffect(() => {
//     if (selectedSessionId) {
//       loadSessionMessages(selectedSessionId);
//     }
//   }, [selectedSessionId]);

//   return (
//     <div className="app-shell">
//       <aside className="sidebar">
//         <div className="sidebar-header">
//           <div>
//             <h1 className="sidebar-title">Confluence RAG Chatbot</h1>
//             <p className="sidebar-subtitle">Sessions</p>
//           </div>
//           <button className="primary-button" onClick={handleCreateNewChat}>
//             New Chat
//           </button>
//         </div>

//         <div className="admin-panel">
//           <div className="admin-panel-title">Knowledge Base Sync</div>
//           <button
//             className="secondary-button"
//             onClick={handleSyncAllPages}
//             disabled={isSyncing}
//           >
//             {isSyncing ? "Syncing..." : "Sync All Pages"}
//           </button>

//           {syncError ? <div className="sync-error">{syncError}</div> : null}

//           {syncResult ? (
//             <div className="sync-summary">
//               <div>
//                 <strong>Space:</strong> {syncResult.space_key}
//               </div>
//               <div>
//                 <strong>Pages Found:</strong> {syncResult.total_pages_found}
//               </div>
//               <div>
//                 <strong>Processed:</strong> {syncResult.total_pages_processed}
//               </div>
//               <div>
//                 <strong>Successful:</strong> {syncResult.total_successful_pages}
//               </div>
//               <div>
//                 <strong>Failed:</strong> {syncResult.total_failed_pages}
//               </div>
//               <div>
//                 <strong>Chunks Upserted:</strong>{" "}
//                 {syncResult.total_chunks_upserted}
//               </div>
//             </div>
//           ) : null}
//         </div>

//         <div className="session-list">
//           {isLoadingSessions ? (
//             <div className="empty-state">Loading sessions...</div>
//           ) : sessions.length === 0 ? (
//             <div className="empty-state">No saved sessions yet.</div>
//           ) : (
//             sessions.map((session) => (
//               <button
//                 key={session.id}
//                 className={
//                   session.id === selectedSessionId
//                     ? "session-item session-item-active"
//                     : "session-item"
//                 }
//                 onClick={() => handleSelectSession(session.id)}
//               >
//                 <div className="session-title">{session.title}</div>
//                 <div className="session-time">
//                   {new Date(session.updated_at).toLocaleString()}
//                 </div>
//               </button>
//             ))
//           )}
//         </div>
//       </aside>

//       <main className="chat-panel">
//         <div className="chat-header">
//           <div>
//             <h2 className="chat-title">
//               {selectedSession ? selectedSession.title : "New conversation"}
//             </h2>
//             <p className="chat-subtitle">
//               Ask questions grounded in your Confluence knowledge base.
//             </p>
//           </div>
//         </div>

//         <div className="messages-area">
//           {messages.length === 0 ? (
//             <div className="welcome-card">
//               <h3>Start chatting</h3>
//               <p>
//                 Ask something like:
//                 <br />
//                 “How do I set up Python for the banking chatbot environment?”
//               </p>
//             </div>
//           ) : (
//             messages.map((message) => (
//               <div
//                 key={message.id}
//                 className={
//                   message.role === "user"
//                     ? "message-row message-row-user"
//                     : "message-row message-row-assistant"
//                 }
//               >
//                 <div
//                   className={
//                     message.role === "user"
//                       ? "message-bubble message-bubble-user"
//                       : "message-bubble message-bubble-assistant"
//                   }
//                 >
//                   <div className="message-role">
//                     {message.role === "user" ? "You" : "Assistant"}
//                   </div>
//                   <div className="message-content">{message.content}</div>

//                   {message.role === "assistant" &&
//                     message.sources &&
//                     message.sources.length > 0 && (
//                       <div className="sources-block">
//                         <div className="sources-title">Sources</div>
//                         <ul className="sources-list">
//                           {message.sources.map((source) => (
//                             <li key={`${source.page_id}-${source.source_url}`}>
//                               <a
//                                 href={source.source_url}
//                                 target="_blank"
//                                 rel="noreferrer"
//                               >
//                                 {source.page_title}
//                               </a>
//                             </li>
//                           ))}
//                         </ul>
//                       </div>
//                     )}
//                 </div>
//               </div>
//             ))
//           )}
//         </div>

//         {error ? <div className="error-banner">{error}</div> : null}

//         <div className="composer">
//           <textarea
//             className="composer-input"
//             placeholder="Ask a question about your Confluence docs..."
//             value={input}
//             onChange={(e) => setInput(e.target.value)}
//             rows={3}
//           />
//           <button
//             className="primary-button composer-button"
//             onClick={handleSendMessage}
//             disabled={isSending}
//           >
//             {isSending ? "Sending..." : "Send"}
//           </button>
//         </div>
//       </main>
//     </div>
//   );
// }

"use client";

import { useEffect, useMemo, useState } from "react";
import {
  BulkUpsertResponse,
  ChatResponse,
  SessionDetailResponse,
  SessionSummary,
  createSession,
  deleteSession,
  getSessionDetail,
  getSessions,
  sendChatMessage,
  syncAllPages,
} from "@/lib/api";

type DisplayMessage = {
  id: string;
  role: "user" | "assistant";
  content: string;
  createdAt?: string;
  sources?: ChatResponse["sources"];
};

export default function ChatApp() {
  const [sessions, setSessions] = useState<SessionSummary[]>([]);
  const [selectedSessionId, setSelectedSessionId] = useState<string | null>(
    null,
  );
  const [messages, setMessages] = useState<DisplayMessage[]>([]);
  const [input, setInput] = useState("");
  const [isLoadingSessions, setIsLoadingSessions] = useState(true);
  const [isSending, setIsSending] = useState(false);
  const [isSyncing, setIsSyncing] = useState(false);
  const [deletingSessionId, setDeletingSessionId] = useState<string | null>(
    null,
  );
  const [error, setError] = useState("");
  const [syncError, setSyncError] = useState("");
  const [syncResult, setSyncResult] = useState<BulkUpsertResponse | null>(null);

  const selectedSession = useMemo(
    () => sessions.find((session) => session.id === selectedSessionId) || null,
    [sessions, selectedSessionId],
  );

  async function refreshSessions(keepCurrentSelection = true) {
    const data = await getSessions();
    setSessions(data.sessions);

    if (
      keepCurrentSelection &&
      !selectedSessionId &&
      data.sessions.length > 0
    ) {
      setSelectedSessionId(data.sessions[0].id);
    }
  }

  async function loadSessions(keepCurrentSelection = true) {
    try {
      await refreshSessions(keepCurrentSelection);
    } catch {
      setError("Failed to load sessions.");
    } finally {
      setIsLoadingSessions(false);
    }
  }

  async function loadSessionMessages(sessionId: string) {
    try {
      const detail: SessionDetailResponse = await getSessionDetail(sessionId);

      const normalizedMessages: DisplayMessage[] = detail.messages.map(
        (message) => ({
          id: String(message.id),
          role: message.role,
          content: message.content,
          createdAt: message.created_at,
          sources: message.sources ?? [],
        }),
      );

      setMessages(normalizedMessages);
    } catch {
      setError("Failed to load session messages.");
    }
  }

  async function handleCreateNewChat() {
    setError("");

    try {
      const session = await createSession();
      await refreshSessions(false);
      setSelectedSessionId(session.id);
      setMessages([]);
    } catch {
      setError("Failed to create a new chat.");
    }
  }

  async function handleSelectSession(sessionId: string) {
    setSelectedSessionId(sessionId);
    await loadSessionMessages(sessionId);
  }

  async function handleDeleteSession(sessionId: string) {
    const confirmed = window.confirm("Delete this chat session permanently?");

    if (!confirmed) {
      return;
    }

    setError("");
    setDeletingSessionId(sessionId);

    try {
      await deleteSession(sessionId);

      const remainingSessions = sessions.filter(
        (session) => session.id !== sessionId,
      );
      setSessions(remainingSessions);

      if (selectedSessionId === sessionId) {
        if (remainingSessions.length > 0) {
          const nextSessionId = remainingSessions[0].id;
          setSelectedSessionId(nextSessionId);
          await loadSessionMessages(nextSessionId);
        } else {
          setSelectedSessionId(null);
          setMessages([]);
        }
      }
    } catch {
      setError("Failed to delete session.");
    } finally {
      setDeletingSessionId(null);
    }
  }

  async function handleSendMessage() {
    const trimmed = input.trim();

    if (!trimmed || isSending) {
      return;
    }

    setError("");
    setIsSending(true);

    try {
      let currentSessionId = selectedSessionId;

      if (!currentSessionId) {
        const newSession = await createSession();
        currentSessionId = newSession.id;
        setSelectedSessionId(newSession.id);
      }

      await sendChatMessage({
        message: trimmed,
        sessionId: currentSessionId ?? undefined,
        k: 4,
      });

      setInput("");

      if (currentSessionId) {
        await loadSessionMessages(currentSessionId);
      }

      await refreshSessions(false);
    } catch {
      setError("Failed to send message.");
    } finally {
      setIsSending(false);
    }
  }

  async function handleSyncAllPages() {
    setSyncError("");
    setSyncResult(null);
    setIsSyncing(true);

    try {
      const result = await syncAllPages({
        limit: 25,
        chunkSize: 800,
        chunkOverlap: 150,
      });
      setSyncResult(result);
    } catch {
      setSyncError("Failed to sync Confluence pages.");
    } finally {
      setIsSyncing(false);
    }
  }

  useEffect(() => {
    loadSessions();
  }, []);

  useEffect(() => {
    if (selectedSessionId) {
      loadSessionMessages(selectedSessionId);
    }
  }, [selectedSessionId]);

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="sidebar-header">
          <div>
            <h1 className="sidebar-title">Confluence RAG Chatbot</h1>
            <p className="sidebar-subtitle">Sessions</p>
          </div>
          <button className="primary-button" onClick={handleCreateNewChat}>
            New Chat
          </button>
        </div>

        <div className="admin-panel">
          <div className="admin-panel-title">Knowledge Base Sync</div>
          <button
            className="secondary-button"
            onClick={handleSyncAllPages}
            disabled={isSyncing}
          >
            {isSyncing ? "Syncing..." : "Sync All Pages"}
          </button>

          {syncError ? <div className="sync-error">{syncError}</div> : null}

          {syncResult ? (
            <div className="sync-summary">
              <div>
                <strong>Space:</strong> {syncResult.space_key}
              </div>
              <div>
                <strong>Pages Found:</strong> {syncResult.total_pages_found}
              </div>
              <div>
                <strong>Processed:</strong> {syncResult.total_pages_processed}
              </div>
              <div>
                <strong>Successful:</strong> {syncResult.total_successful_pages}
              </div>
              <div>
                <strong>Failed:</strong> {syncResult.total_failed_pages}
              </div>
              <div>
                <strong>Chunks Upserted:</strong>{" "}
                {syncResult.total_chunks_upserted}
              </div>
            </div>
          ) : null}
        </div>

        <div className="session-list">
          {isLoadingSessions ? (
            <div className="empty-state">Loading sessions...</div>
          ) : sessions.length === 0 ? (
            <div className="empty-state">No saved sessions yet.</div>
          ) : (
            sessions.map((session) => (
              <div
                key={session.id}
                className={
                  session.id === selectedSessionId
                    ? "session-row session-row-active"
                    : "session-row"
                }
              >
                <button
                  className="session-item"
                  onClick={() => handleSelectSession(session.id)}
                >
                  <div className="session-title">{session.title}</div>
                  <div className="session-time">
                    {new Date(session.updated_at).toLocaleString()}
                  </div>
                </button>

                <button
                  className="delete-button"
                  onClick={() => handleDeleteSession(session.id)}
                  disabled={deletingSessionId === session.id}
                  title="Delete chat"
                >
                  {deletingSessionId === session.id ? "..." : "🗑"}
                </button>
              </div>
            ))
          )}
        </div>
      </aside>

      <main className="chat-panel">
        <div className="chat-header">
          <div>
            <h2 className="chat-title">
              {selectedSession ? selectedSession.title : "New conversation"}
            </h2>
            <p className="chat-subtitle">
              Ask questions grounded in your Confluence knowledge base.
            </p>
          </div>
        </div>

        <div className="messages-area">
          {messages.length === 0 ? (
            <div className="welcome-card">
              <h3>Start chatting</h3>
              <p>
                Ask something like:
                <br />
                “How do I set up Python for the banking chatbot environment?”
              </p>
            </div>
          ) : (
            messages.map((message) => (
              <div
                key={message.id}
                className={
                  message.role === "user"
                    ? "message-row message-row-user"
                    : "message-row message-row-assistant"
                }
              >
                <div
                  className={
                    message.role === "user"
                      ? "message-bubble message-bubble-user"
                      : "message-bubble message-bubble-assistant"
                  }
                >
                  <div className="message-role">
                    {message.role === "user" ? "You" : "Assistant"}
                  </div>
                  <div className="message-content">{message.content}</div>

                  {message.role === "assistant" &&
                    message.sources &&
                    message.sources.length > 0 && (
                      <div className="sources-block">
                        <div className="sources-title">Sources</div>
                        <ul className="sources-list">
                          {message.sources.map((source) => (
                            <li key={`${source.page_id}-${source.source_url}`}>
                              <a
                                href={source.source_url}
                                target="_blank"
                                rel="noreferrer"
                              >
                                {source.page_title}
                              </a>
                            </li>
                          ))}
                        </ul>
                      </div>
                    )}
                </div>
              </div>
            ))
          )}
        </div>

        {error ? <div className="error-banner">{error}</div> : null}

        <div className="composer">
          <textarea
            className="composer-input"
            placeholder="Ask a question about your Confluence docs..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            rows={3}
          />
          <button
            className="primary-button composer-button"
            onClick={handleSendMessage}
            disabled={isSending}
          >
            {isSending ? "Sending..." : "Send"}
          </button>
        </div>
      </main>
    </div>
  );
}
