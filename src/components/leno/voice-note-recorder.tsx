"use client"

import { AIVoiceInput } from "@/components/ui/ai-voice-input"
import { useAudioRecorder } from "@/hooks/use-audio-recorder"

interface VoiceNoteRecorderProps {
  onRecorded: (blob: Blob, durationMs: number) => void
  className?: string
}

export function VoiceNoteRecorder({ onRecorded, className }: VoiceNoteRecorderProps) {
  const { isRecording, error, start, stop } = useAudioRecorder()

  const handleStart = () => {
    if (!isRecording) {
      void start()
    }
  }

  const handleStop = async () => {
    const result = await stop()
    if (result && result.durationMs > 300) {
      onRecorded(result.blob, result.durationMs)
    }
  }

  return (
    <div className={className}>
      <AIVoiceInput onStart={handleStart} onStop={handleStop} />
      {error && <p className="text-center text-xs text-destructive">{error}</p>}
    </div>
  )
}
