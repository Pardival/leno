"use client"

import { Mic, Square } from "lucide-react"
import { cn } from "@/lib/utils"
import { useAudioRecorder } from "@/hooks/use-audio-recorder"

function formatDuration(ms: number) {
  const totalSeconds = Math.floor(ms / 1000)
  const minutes = Math.floor(totalSeconds / 60)
  const seconds = totalSeconds % 60
  return `${minutes}:${seconds.toString().padStart(2, "0")}`
}

interface RecordZoneProps {
  onRecorded: (blob: Blob, durationMs: number) => void
  className?: string
}

export function RecordZone({ onRecorded, className }: RecordZoneProps) {
  const { isRecording, durationMs, error, start, stop } = useAudioRecorder()

  const handleClick = async () => {
    if (isRecording) {
      const result = await stop()
      if (result && result.durationMs > 300) {
        onRecorded(result.blob, result.durationMs)
      }
    } else {
      await start()
    }
  }

  return (
    <button
      type="button"
      onClick={handleClick}
      aria-pressed={isRecording}
      aria-label={isRecording ? "Stop recording" : "Record a voice note"}
      className={cn(
        "group relative flex w-full shrink-0 flex-col items-center justify-center gap-1.5 rounded-2xl border-2 border-dashed p-4 text-center transition-colors md:w-44",
        isRecording
          ? "border-destructive bg-destructive/5"
          : "border-border bg-secondary/30 hover:border-primary/50 hover:bg-secondary/50",
        className,
      )}
    >
      <span className="relative flex h-12 w-12 items-center justify-center rounded-full bg-background shadow-sm">
        {isRecording && (
          <span className="absolute inset-0 rounded-full bg-destructive/20 animate-ping" />
        )}
        {isRecording ? (
          <Square className="h-4 w-4 fill-destructive text-destructive" />
        ) : (
          <Mic className="h-5 w-5 text-foreground" />
        )}
      </span>
      <span className="text-sm font-medium text-foreground">
        {isRecording ? formatDuration(durationMs) : "Record a note"}
      </span>
      <span className="text-xs text-muted-foreground">
        {isRecording ? "Tap to stop" : "Tap and speak"}
      </span>
      {error && <span className="text-xs text-destructive">{error}</span>}
    </button>
  )
}
