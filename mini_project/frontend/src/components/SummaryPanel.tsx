import { useState } from "react";
import { summarizeText } from "../api/client";

export default function SummaryPanel() {
  const [text, setText] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSummarize = async () => {
    if (!text.trim()) return;

    setLoading(true);
    const result = await summarizeText(text);
    setSummary(result);
    setLoading(false);
  };

  return (
    <div className="flex flex-col h-full p-4 gap-4">
      <h2 className="text-xl font-bold">텍스트 요약</h2>

      {/* 입력 영역 */}
      <textarea
        className="flex-1 border rounded-lg p-3 outline-none resize-none"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="요약할 텍스트를 입력하세요..."
      />

      <button
        className="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600"
        onClick={handleSummarize}
      >
        {loading ? "요약 중..." : "요약하기"}
      </button>

      {/* 요약 결과 */}
      {summary && (
        <div className="border rounded-lg p-4 bg-green-50">
          <h3 className="font-bold mb-2">요약 결과</h3>
          <p className="text-gray-700">{summary}</p>
        </div>
      )}
    </div>
  );
}
