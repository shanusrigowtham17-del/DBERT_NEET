import React from 'react';
import { ChevronLeft, ChevronRight, Check } from 'lucide-react';

const QuestionCard = ({
  question,
  questionNumber,
  totalQuestions,
  selectedOption,
  onSelectOption,
  onPrev,
  onNext,
  hasPrev,
  hasNext,
  isSaving,
}) => {
  if (!question) {
    return (
      <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-200 text-center text-gray-500">
        No question selected.
      </div>
    );
  }

  const options = [
    { key: 'A', text: question.option_a },
    { key: 'B', text: question.option_b },
    { key: 'C', text: question.option_c },
    { key: 'D', text: question.option_d },
  ];

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden flex flex-col">
      {/* Header */}
      <div className="px-6 py-4 border-b border-gray-100 flex items-center justify-between bg-gray-50/50">
        <div className="flex items-center space-x-2">
          <span className="text-xs font-semibold uppercase tracking-wider text-indigo-600 bg-indigo-50 px-2.5 py-1 rounded">
            Question {questionNumber} of {totalQuestions}
          </span>
          {question.difficulty && (
            <span className="text-xs font-medium text-gray-500 capitalize">
              • {question.difficulty}
            </span>
          )}
        </div>
        {isSaving && (
          <span className="text-xs text-gray-400 italic flex items-center">
            <span className="w-1.5 h-1.5 bg-indigo-500 rounded-full animate-ping mr-1.5"></span>
            Saving...
          </span>
        )}
      </div>

      {/* Question Text */}
      <div className="p-6">
        <p className="text-lg font-medium text-gray-900 leading-relaxed whitespace-pre-wrap">
          {question.text}
        </p>
      </div>

      {/* Options */}
      <div className="px-6 pb-6 space-y-3">
        {options.map(({ key, text }) => {
          const isSelected = selectedOption === key;
          return (
            <button
              key={key}
              type="button"
              onClick={() => onSelectOption(key)}
              className={`w-full text-left p-4 rounded-xl border-2 transition-all duration-150 flex items-start space-x-3.5 ${
                isSelected
                  ? 'border-indigo-600 bg-indigo-50/50 shadow-sm'
                  : 'border-gray-200 hover:border-gray-300 hover:bg-gray-50/50'
              }`}
            >
              <div
                className={`w-7 h-7 rounded-lg flex items-center justify-center font-semibold text-sm flex-shrink-0 transition-colors ${
                  isSelected
                    ? 'bg-indigo-600 text-white shadow-sm'
                    : 'bg-gray-100 text-gray-700'
                }`}
              >
                {isSelected ? <Check className="w-4 h-4" /> : key}
              </div>
              <span className={`text-base pt-0.5 ${isSelected ? 'font-medium text-indigo-950' : 'text-gray-800'}`}>
                {text}
              </span>
            </button>
          );
        })}
      </div>

      {/* Footer Navigation */}
      <div className="px-6 py-4 bg-gray-50 border-t border-gray-100 flex items-center justify-between mt-auto">
        <button
          type="button"
          onClick={onPrev}
          disabled={!hasPrev}
          className={`flex items-center space-x-1 px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
            hasPrev
              ? 'text-gray-700 bg-white border border-gray-300 hover:bg-gray-100'
              : 'text-gray-300 bg-gray-100 border border-transparent cursor-not-allowed'
          }`}
        >
          <ChevronLeft className="w-4 h-4" />
          <span>Previous</span>
        </button>

        {selectedOption && (
          <button
            type="button"
            onClick={() => onSelectOption(null)}
            className="text-xs text-gray-500 hover:text-red-600 hover:underline transition-colors"
          >
            Clear Choice
          </button>
        )}

        <button
          type="button"
          onClick={onNext}
          disabled={!hasNext}
          className={`flex items-center space-x-1 px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
            hasNext
              ? 'text-white bg-indigo-600 hover:bg-indigo-700 shadow-sm'
              : 'text-gray-400 bg-gray-200 cursor-not-allowed'
          }`}
        >
          <span>Next</span>
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};

export default QuestionCard;

