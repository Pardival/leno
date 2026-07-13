"use client"

import { useCallback, useRef, useState } from "react"

export interface RecordingResult {
  blob: Blob
  durationMs: number
}

export interface UseAudioRecorderResult {
  isRecording: boolean
  durationMs: number
  error: string | null
  start: () => Promise<void>
  stop: () => Promise<RecordingResult | null>
}

export function useAudioRecorder(): UseAudioRecorderResult {
  const [isRecording, setIsRecording] = useState(false)
  const [durationMs, setDurationMs] = useState(0)
  const [error, setError] = useState<string | null>(null)

  const mediaRecorderRef = useRef<MediaRecorder | null>(null)
  const chunksRef = useRef<Blob[]>([])
  const streamRef = useRef<MediaStream | null>(null)
  const startTimeRef = useRef(0)
  const intervalRef = useRef<ReturnType<typeof setInterval> | null>(null)

  const start = useCallback(async () => {
    setError(null)
    if (typeof window === "undefined" || !navigator.mediaDevices?.getUserMedia) {
      setError("Voice recording isn't supported in this browser.")
      return
    }

    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
      streamRef.current = stream

      const mediaRecorder = new MediaRecorder(stream)
      chunksRef.current = []
      mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) chunksRef.current.push(event.data)
      }
      mediaRecorder.start()
      mediaRecorderRef.current = mediaRecorder

      startTimeRef.current = Date.now()
      setDurationMs(0)
      intervalRef.current = setInterval(() => {
        setDurationMs(Date.now() - startTimeRef.current)
      }, 100)
      setIsRecording(true)
    } catch {
      setError("Microphone access was denied or is unavailable.")
    }
  }, [])

  const stop = useCallback(async (): Promise<RecordingResult | null> => {
    const mediaRecorder = mediaRecorderRef.current
    if (!mediaRecorder) return null

    return new Promise((resolve) => {
      mediaRecorder.onstop = () => {
        const blob = new Blob(chunksRef.current, {
          type: mediaRecorder.mimeType || "audio/webm",
        })
        const finalDuration = Date.now() - startTimeRef.current

        streamRef.current?.getTracks().forEach((track) => track.stop())
        streamRef.current = null
        mediaRecorderRef.current = null

        if (intervalRef.current) {
          clearInterval(intervalRef.current)
          intervalRef.current = null
        }

        setIsRecording(false)
        resolve({ blob, durationMs: finalDuration })
      }
      mediaRecorder.stop()
    })
  }, [])

  return { isRecording, durationMs, error, start, stop }
}
