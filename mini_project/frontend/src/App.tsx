import { useState } from "react";
import ChatWindow from "./components/ChatWindow";
import SummaryPanel from "./components/SummaryPanel";

export default function App() {
  const [tab, setTab] = useState<"chat" | "summary">("chat");

  return (
    <div className="flex flex-col h-screen bg-gray-100">
      {/* 헤더 */}
      <header
        className="bg-blue-600 text-white p-4 text-xl font-bold"
        style={{ fontFamily: "'Black Ops One', cursive" }}
      >
        AI Chat Bot
      </header>

      {/* 탭 */}
      <div className="flex border-b bg-white">
        <button
          className={`px-6 py-3 font-medium ${
            tab === "chat"
              ? "border-b-2 border-blue-500 text-blue-500"
              : "text-gray-500"
          }`}
          onClick={() => setTab("chat")}
        >
          채팅
        </button>
        <button
          className={`px-6 py-3 font-medium ${
            tab === "summary"
              ? "border-b-2 border-blue-500 text-blue-500"
              : "text-gray-500"
          }`}
          onClick={() => setTab("summary")}
        >
          텍스트 요약
        </button>
      </div>

      {/* 컨텐츠 */}
      <main className="flex-1 overflow-hidden bg-white">
        {tab === "chat" ? <ChatWindow /> : <SummaryPanel />}
      </main>
    </div>
  );
}
