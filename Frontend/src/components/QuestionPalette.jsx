import React from 'react';

const QuestionPalette = ({
  totalQuestions,
  currentIndex,
  answers, // map of { [questionId]: selectedOption }
  questions, // array of question objects
  onSelectQuestion,
}) => {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-5">
      <h3 className="text-sm font-semibold text-gray-900 mb-3 uppercase tracking-wider">
        Question Palette
      </h3>

      {/* Legend */}
      <div className="flex flex-wrap gap-2 text-xs mb-4 pb-3 border-b border-gray-100">
        <div className="flex items-center space-x-1.5">
          <span className="w-3 h-3 rounded bg-emerald-500"></span>
          <span className="text-gray-600">Answered</span>
        </div>
        <div className="flex items-center space-x-1.5">
          <span className="w-3 h-3 rounded bg-gray-200 border border-gray-300"></span>
          <span className="text-gray-600">Unanswered</span>
        </div>
        <div className="flex items-center space-x-1.5">
          <span className="w-3 h-3 rounded ring-2 ring-indigo-600 bg-white border border-indigo-600"></span>
          <span className="text-gray-600">Current</span>
        </div>
      </div>

      {/* Grid of buttons */}
      <div className="grid grid-cols-5 sm:grid-cols-6 md:grid-cols-5 gap-2 max-h-[350px] overflow-y-auto pr-1">
        {questions.map((q, idx) => {
          const isCurrent = idx === currentIndex;
          const isAnswered = Boolean(answers && answers[q.id]);

          let btnClass = 'bg-gray-100 text-gray-700 hover:bg-gray-200 border border-gray-200';
          if (isAnswered) {
            btnClass = 'bg-emerald-500 text-white hover:bg-emerald-600 border border-emerald-600 shadow-sm';
          }
          if (isCurrent) {
            btnClass += ' ring-2 ring-indigo-600 ring-offset-2 font-bold';
          }

          return (
            <button
              key={q.id || idx}
              type="button"
              onClick={() => onSelectQuestion(idx)}
              className={`h-9 w-full rounded-lg text-sm font-semibold transition-all duration-150 flex items-center justify-center ${btnClass}`}
              title={`Question ${idx + 1}: ${isAnswered ? 'Answered' : 'Unanswered'}`}
            >
              {idx + 1}
            </button>
          );
        })}
      </div>

      {/* Summary stats */}
      <div className="mt-4 pt-3 border-t border-gray-100 flex justify-between text-xs text-gray-500">
        <span>Answered: {Object.values(answers || {}).filter(Boolean).length}</span>
        <span>Remaining: {totalQuestions - Object.values(answers || {}).filter(Boolean).length}</span>
      </div>
    </div>
  );
};

export default QuestionPalette;

