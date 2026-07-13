"use client"

import { useState } from "react"
import { Send } from "lucide-react"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"

interface NoteComposerProps {
  onAddTextNote: (text: string) => void
  className?: string
}

export function NoteComposer({ onAddTextNote, className }: NoteComposerProps) {
  const [value, setValue] = useState("")

  const submit = () => {
    const trimmed = value.trim()
    if (!trimmed) return
    onAddTextNote(trimmed)
    setValue("")
  }

  return (
    <div
      className={cn(
        "flex flex-1 items-end gap-2 rounded-2xl border border-border bg-card p-3 shadow-sm",
        className,
      )}
    >
      <Textarea
        value={value}
        onChange={(event) => setValue(event.target.value)}
        onKeyDown={(event) => {
          if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault()
            submit()
          }
        }}
        placeholder="Note down what's on your mind..."
        className="max-h-48 min-h-11 resize-none border-none bg-transparent px-1 py-2 shadow-none focus-visible:ring-0"
        rows={1}
      />
      <Button
        type="button"
        size="icon-lg"
        onClick={submit}
        disabled={!value.trim()}
        aria-label="Save note"
      >
        <Send className="h-4 w-4" />
      </Button>
    </div>
  )
}
