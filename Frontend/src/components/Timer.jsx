import React, { useState, useEffect, useRef } from 'react';
import { Clock, AlertTriangle } from 'lucide-react';

/**
 * Safely parse a datetime string into a Date object in UTC.
 * If the string lacks a timezone offset (e.g., '2026-09-16T14:16:12' or '2026-09-16 14:16:12'),
 * appends 'Z' to treat it strictly as UTC, matching the backend's datetime.now(timezone.utc).
 */
export const parseUtcDate = (dateVal) => {
  if (!dateVal) return null;
  if (dateVal instanceof Date) return dateVal;
  if (typeof dateVal === 'string') {
    let s = dateVal.trim().replace(' ', 'T');
    // If no timezone offset is present (+/-HH:MM or Z)
    if (!s.endsWith('Z') && !/[+-]\d{2}:\d{2}$/.test(s)) {
      s += 'Z';
    }
    const d = new Date(s);
    return isNaN(d.getTime()) ? null : d;
  }
  const d = new Date(dateVal);
  return isNaN(d.getTime()) ? null : d;
};

const Timer = ({ startedAt, durationSeconds, onExpire }) => {
  const getDiffSeconds = () => {
    if (!startedAt || !durationSeconds) return null;
    const startDate = parseUtcDate(startedAt);
    if (!startDate) return null;
    const startTimeMs = startDate.getTime();
    const expiryTimeMs = startTimeMs + durationSeconds * 1000;
    const diffSeconds = Math.floor((expiryTimeMs - Date.now()) / 1000);
    return Math.max(0, diffSeconds);
  };

  const [secondsLeft, setSecondsLeft] = useState(() => {
    const initial = getDiffSeconds();
    return initial !== null ? initial : durationSeconds || 0;
  });

  const onExpireRef = useRef(onExpire);
  onExpireRef.current = onExpire;
  const hasExpiredTriggered = useRef(false);
  const mountTimeRef = useRef(Date.now());

  useEffect(() => {
    if (!startedAt || !durationSeconds) return;

    // Calculate remaining time upon effect trigger
    const initial = getDiffSeconds();
    if (initial !== null) {
      setSecondsLeft(initial);
      // If truly expired (and at least 1.5s has elapsed since mount to prevent race conditions on initial mount)
      if (initial <= 0 && !hasExpiredTriggered.current && Date.now() - mountTimeRef.current > 1500) {
        hasExpiredTriggered.current = true;
        if (onExpireRef.current) {
          onExpireRef.current();
        }
        return;
      }
    }

    const interval = setInterval(() => {
      const remaining = getDiffSeconds();
      if (remaining === null) return;

      setSecondsLeft(remaining);

      if (remaining <= 0 && !hasExpiredTriggered.current) {
        hasExpiredTriggered.current = true;
        clearInterval(interval);
        if (onExpireRef.current) {
          onExpireRef.current();
        }
      }
    }, 1000);

    return () => clearInterval(interval);
  }, [startedAt, durationSeconds]);

  // Format HH:MM:SS
  const formatTime = (totalSeconds) => {
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;

    const pad = (n) => String(n).padStart(2, '0');

    if (hours > 0) {
      return `${pad(hours)}:${pad(minutes)}:${pad(seconds)}`;
    }
    return `${pad(minutes)}:${pad(seconds)}`;
  };

  const isLowTime = secondsLeft <= 300; // 5 minutes or less
  const isUrgent = secondsLeft <= 60; // 1 minute or less

  return (
    <div
      className={`flex items-center space-x-2 px-3.5 py-1.5 rounded-lg font-mono font-bold text-sm tracking-wider shadow-sm transition-colors duration-300 ${
        isUrgent
          ? 'bg-red-100 text-red-700 border border-red-300 animate-pulse'
          : isLowTime
          ? 'bg-amber-50 text-amber-800 border border-amber-300'
          : 'bg-indigo-50 text-indigo-700 border border-indigo-200'
      }`}
    >
      {isUrgent ? (
        <AlertTriangle className="w-4 h-4 text-red-600 animate-bounce" />
      ) : (
        <Clock className="w-4 h-4" />
      )}
      <span>{formatTime(secondsLeft)}</span>
    </div>
  );
};

export default Timer;
