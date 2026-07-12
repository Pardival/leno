"use client"

import { useCallback, useRef, useState } from "react"
import { Mic, Type } from "lucide-react"
import { Component as MorphingCardStack, type CardData } from "@/components/ui/morphing-card-stack"
import { NoteComposer } from "@/components/leno/note-composer"
import { RecordZone } from "@/components/leno/record-zone"

function formatClockDuration(ms: number) {
  const totalSeconds = Math.max(1, Math.round(ms / 1000))
  const minutes = Math.floor(totalSeconds / 60)
  const seconds = totalSeconds % 60
  return `${minutes}:${seconds.toString().padStart(2, "0")}`
}

function truncate(text: string, max = 40) {
  return text.length > max ? `${text.slice(0, max).trimEnd()}…` : text
}

export function NotesBoard() {
  const [notes, setNotes] = useState<CardData[]>([])
  const voiceAudioUrls = useRef<Map<string, string>>(new Map())
  const audioElRef = useRef<HTMLAudioElement | null>(null)
  const idRef = useRef(0)

  const nextId = () => {
    idRef.current += 1
    return `note-${idRef.current}-${Date.now()}`
  }

  const addTextNote = useCallback((text: string) => {
    const id = nextId()
    setNotes((prev) => [
      {
        id,
        title: truncate(text),
        description: text,
        icon: <Type className="h-5 w-5" />,
      },
      ...prev,
    ])
  }, [])

  const addVoiceNote = useCallback((blob: Blob, durationMs: number) => {
    const id = nextId()
    voiceAudioUrls.current.set(id, URL.createObjectURL(blob))
    setNotes((prev) => [
      {
        id,
        title: "Voice note",
        description: `${formatClockDuration(durationMs)} · tap to play`,
        icon: <Mic className="h-5 w-5" />,
      },
      ...prev,
    ])
  }, [])

  const handleCardClick = useCallback((card: CardData) => {
    const audioUrl = voiceAudioUrls.current.get(card.id)
    if (!audioUrl) return

    if (!audioElRef.current) {
      audioElRef.current = new Audio()
    }
    const audioEl = audioElRef.current

    if (audioEl.src === audioUrl && !audioEl.paused) {
      audioEl.pause()
      return
    }
    audioEl.src = audioUrl
    void audioEl.play()
  }, [])

  return (
    <div className="flex w-full max-w-3xl flex-col gap-6">
      <div className="flex flex-col gap-3 md:flex-row">
        <NoteComposer onAddTextNote={addTextNote} />
        <RecordZone onRecorded={addVoiceNote} />
      </div>

      {notes.length > 0 ? (
        <MorphingCardStack cards={notes} onCardClick={handleCardClick} />
      ) : (
        <div className="rounded-2xl border border-dashed border-border p-10 text-center text-sm text-muted-foreground">
          Your notes will show up here, connected and classified automatically.
        </div>
      )}
    </div>
  )
}
