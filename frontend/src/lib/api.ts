// const API_BASE_URL =
//   process.env.NEXT_PUBLIC_API_BASE_URL || "http://127.0.0.1:8000";

// export type SessionSummary = {
//   id: string;
//   title: string;
//   created_at: string;
//   updated_at: string;
// };

// export type SessionListResponse = {
//   count: number;
//   sessions: SessionSummary[];
// };

// export type SessionMessage = {
//   id: number;
//   role: "user" | "assistant";
//   content: string;
//   created_at: string;
// };

// export type SessionDetailResponse = {
//   id: string;
//   title: string;
//   created_at: string;
//   updated_at: string;
//   messages: SessionMessage[];
// };

// export type ChatSource = {
//   page_id: string;
//   page_title: string;
//   source_url: string;
// };

// export type ChatResponse = {
//   session_id: string;
//   user_message: string;
//   bot_reply: string;
//   sources: ChatSource[];
//   retrieved_chunk_count: number;
// };

// export async function getSessions(): Promise<SessionListResponse> {
//   const response = await fetch(`${API_BASE_URL}/sessions`, {
//     cache: "no-store",
//   });

//   if (!response.ok) {
//     throw new Error("Failed to fetch sessions");
//   }

//   return response.json();
// }

// export async function createSession(title?: string): Promise<SessionSummary> {
//   const response = await fetch(`${API_BASE_URL}/sessions`, {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({
//       title: title || null,
//     }),
//   });

//   if (!response.ok) {
//     throw new Error("Failed to create session");
//   }

//   return response.json();
// }

// export async function getSessionDetail(
//   sessionId: string,
// ): Promise<SessionDetailResponse> {
//   const response = await fetch(`${API_BASE_URL}/sessions/${sessionId}`, {
//     cache: "no-store",
//   });

//   if (!response.ok) {
//     throw new Error("Failed to fetch session detail");
//   }

//   return response.json();
// }

// export async function sendChatMessage(params: {
//   message: string;
//   sessionId?: string;
//   k?: number;
// }): Promise<ChatResponse> {
//   const response = await fetch(`${API_BASE_URL}/chat`, {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({
//       message: params.message,
//       session_id: params.sessionId ?? null,
//       k: params.k ?? 4,
//     }),
//   });

//   if (!response.ok) {
//     const text = await response.text();
//     throw new Error(text || "Failed to send message");
//   }

//   return response.json();
// }

// const API_BASE_URL =
//   process.env.NEXT_PUBLIC_API_BASE_URL || "http://127.0.0.1:8000";

// export type ChatSource = {
//   page_id: string;
//   page_title: string;
//   source_url: string;
// };

// export type SessionSummary = {
//   id: string;
//   title: string;
//   created_at: string;
//   updated_at: string;
// };

// export type SessionListResponse = {
//   count: number;
//   sessions: SessionSummary[];
// };

// export type SessionMessage = {
//   id: number;
//   role: "user" | "assistant";
//   content: string;
//   created_at: string;
//   sources: ChatSource[];
// };

// export type SessionDetailResponse = {
//   id: string;
//   title: string;
//   created_at: string;
//   updated_at: string;
//   messages: SessionMessage[];
// };

// export type ChatResponse = {
//   session_id: string;
//   user_message: string;
//   bot_reply: string;
//   sources: ChatSource[];
//   retrieved_chunk_count: number;
// };

// export async function getSessions(): Promise<SessionListResponse> {
//   const response = await fetch(`${API_BASE_URL}/sessions`, {
//     cache: "no-store",
//   });

//   if (!response.ok) {
//     throw new Error("Failed to fetch sessions");
//   }

//   return response.json();
// }

// export async function createSession(title?: string): Promise<SessionSummary> {
//   const response = await fetch(`${API_BASE_URL}/sessions`, {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({
//       title: title || null,
//     }),
//   });

//   if (!response.ok) {
//     throw new Error("Failed to create session");
//   }

//   return response.json();
// }

// export async function getSessionDetail(
//   sessionId: string,
// ): Promise<SessionDetailResponse> {
//   const response = await fetch(`${API_BASE_URL}/sessions/${sessionId}`, {
//     cache: "no-store",
//   });

//   if (!response.ok) {
//     throw new Error("Failed to fetch session detail");
//   }

//   return response.json();
// }

// export async function sendChatMessage(params: {
//   message: string;
//   sessionId?: string;
//   k?: number;
// }): Promise<ChatResponse> {
//   const response = await fetch(`${API_BASE_URL}/chat`, {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({
//       message: params.message,
//       session_id: params.sessionId ?? null,
//       k: params.k ?? 4,
//     }),
//   });

//   if (!response.ok) {
//     const text = await response.text();
//     throw new Error(text || "Failed to send message");
//   }

//   return response.json();
// }

// working without delete button
// const API_BASE_URL =
//   process.env.NEXT_PUBLIC_API_BASE_URL || "http://127.0.0.1:8000";

// export type ChatSource = {
//   page_id: string;
//   page_title: string;
//   source_url: string;
// };

// export type SessionSummary = {
//   id: string;
//   title: string;
//   created_at: string;
//   updated_at: string;
// };

// export type SessionListResponse = {
//   count: number;
//   sessions: SessionSummary[];
// };

// export type SessionMessage = {
//   id: number;
//   role: "user" | "assistant";
//   content: string;
//   created_at: string;
//   sources: ChatSource[];
// };

// export type SessionDetailResponse = {
//   id: string;
//   title: string;
//   created_at: string;
//   updated_at: string;
//   messages: SessionMessage[];
// };

// export type ChatResponse = {
//   session_id: string;
//   user_message: string;
//   bot_reply: string;
//   sources: ChatSource[];
//   retrieved_chunk_count: number;
// };

// export type BulkUpsertPageResult = {
//   page_id: string;
//   page_title: string;
//   success: boolean;
//   chunk_count: number;
//   error?: string | null;
// };

// export type BulkUpsertResponse = {
//   space_key: string;
//   total_pages_found: number;
//   total_pages_processed: number;
//   total_successful_pages: number;
//   total_failed_pages: number;
//   total_chunks_upserted: number;
//   collection_name: string;
//   results: BulkUpsertPageResult[];
// };

// export async function getSessions(): Promise<SessionListResponse> {
//   const response = await fetch(`${API_BASE_URL}/sessions`, {
//     cache: "no-store",
//   });

//   if (!response.ok) {
//     throw new Error("Failed to fetch sessions");
//   }

//   return response.json();
// }

// export async function createSession(title?: string): Promise<SessionSummary> {
//   const response = await fetch(`${API_BASE_URL}/sessions`, {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({
//       title: title || null,
//     }),
//   });

//   if (!response.ok) {
//     throw new Error("Failed to create session");
//   }

//   return response.json();
// }

// export async function getSessionDetail(
//   sessionId: string,
// ): Promise<SessionDetailResponse> {
//   const response = await fetch(`${API_BASE_URL}/sessions/${sessionId}`, {
//     cache: "no-store",
//   });

//   if (!response.ok) {
//     throw new Error("Failed to fetch session detail");
//   }

//   return response.json();
// }

// export async function sendChatMessage(params: {
//   message: string;
//   sessionId?: string;
//   k?: number;
// }): Promise<ChatResponse> {
//   const response = await fetch(`${API_BASE_URL}/chat`, {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({
//       message: params.message,
//       session_id: params.sessionId ?? null,
//       k: params.k ?? 4,
//     }),
//   });

//   if (!response.ok) {
//     const text = await response.text();
//     throw new Error(text || "Failed to send message");
//   }

//   return response.json();
// }

// export async function syncAllPages(params?: {
//   limit?: number;
//   chunkSize?: number;
//   chunkOverlap?: number;
// }): Promise<BulkUpsertResponse> {
//   const limit = params?.limit ?? 25;
//   const chunkSize = params?.chunkSize ?? 800;
//   const chunkOverlap = params?.chunkOverlap ?? 150;

//   const url = new URL(`${API_BASE_URL}/ingest/space/upsert`);
//   url.searchParams.set("limit", String(limit));
//   url.searchParams.set("chunk_size", String(chunkSize));
//   url.searchParams.set("chunk_overlap", String(chunkOverlap));

//   const response = await fetch(url.toString(), {
//     method: "POST",
//   });

//   if (!response.ok) {
//     const text = await response.text();
//     throw new Error(text || "Failed to sync Confluence pages");
//   }

//   return response.json();
// }

const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_BASE_URL || "http://127.0.0.1:8000";

export type ChatSource = {
  page_id: string;
  page_title: string;
  source_url: string;
};

export type SessionSummary = {
  id: string;
  title: string;
  created_at: string;
  updated_at: string;
};

export type SessionListResponse = {
  count: number;
  sessions: SessionSummary[];
};

export type SessionMessage = {
  id: number;
  role: "user" | "assistant";
  content: string;
  created_at: string;
  sources: ChatSource[];
};

export type SessionDetailResponse = {
  id: string;
  title: string;
  created_at: string;
  updated_at: string;
  messages: SessionMessage[];
};

export type ChatResponse = {
  session_id: string;
  user_message: string;
  bot_reply: string;
  sources: ChatSource[];
  retrieved_chunk_count: number;
};

export type BulkUpsertPageResult = {
  page_id: string;
  page_title: string;
  success: boolean;
  chunk_count: number;
  error?: string | null;
};

export type BulkUpsertResponse = {
  space_key: string;
  total_pages_found: number;
  total_pages_processed: number;
  total_successful_pages: number;
  total_failed_pages: number;
  total_chunks_upserted: number;
  collection_name: string;
  results: BulkUpsertPageResult[];
};

export async function getSessions(): Promise<SessionListResponse> {
  const response = await fetch(`${API_BASE_URL}/sessions`, {
    cache: "no-store",
  });

  if (!response.ok) {
    throw new Error("Failed to fetch sessions");
  }

  return response.json();
}

export async function createSession(title?: string): Promise<SessionSummary> {
  const response = await fetch(`${API_BASE_URL}/sessions`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      title: title || null,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to create session");
  }

  return response.json();
}

export async function deleteSession(sessionId: string): Promise<void> {
  const response = await fetch(`${API_BASE_URL}/sessions/${sessionId}`, {
    method: "DELETE",
  });

  if (!response.ok) {
    const text = await response.text();
    throw new Error(text || "Failed to delete session");
  }
}

export async function getSessionDetail(
  sessionId: string,
): Promise<SessionDetailResponse> {
  const response = await fetch(`${API_BASE_URL}/sessions/${sessionId}`, {
    cache: "no-store",
  });

  if (!response.ok) {
    throw new Error("Failed to fetch session detail");
  }

  return response.json();
}

export async function sendChatMessage(params: {
  message: string;
  sessionId?: string;
  k?: number;
}): Promise<ChatResponse> {
  const response = await fetch(`${API_BASE_URL}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message: params.message,
      session_id: params.sessionId ?? null,
      k: params.k ?? 4,
    }),
  });

  if (!response.ok) {
    const text = await response.text();
    throw new Error(text || "Failed to send message");
  }

  return response.json();
}

export async function syncAllPages(params?: {
  limit?: number;
  chunkSize?: number;
  chunkOverlap?: number;
}): Promise<BulkUpsertResponse> {
  const limit = params?.limit ?? 25;
  const chunkSize = params?.chunkSize ?? 800;
  const chunkOverlap = params?.chunkOverlap ?? 150;

  const url = new URL(`${API_BASE_URL}/ingest/space/upsert`);
  url.searchParams.set("limit", String(limit));
  url.searchParams.set("chunk_size", String(chunkSize));
  url.searchParams.set("chunk_overlap", String(chunkOverlap));

  const response = await fetch(url.toString(), {
    method: "POST",
  });

  if (!response.ok) {
    const text = await response.text();
    throw new Error(text || "Failed to sync Confluence pages");
  }

  return response.json();
}
