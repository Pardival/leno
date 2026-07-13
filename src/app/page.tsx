import { Logo } from "@/components/leno/logo"
import { NotesBoard } from "@/components/leno/notes-board"

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col items-center bg-zinc-50 px-6 py-16 dark:bg-black">
      <header className="mb-10 flex max-w-xl flex-col items-center gap-4 text-center">
        <div className="flex items-center gap-2">
          <Logo className="h-12 w-12" />
          <span className="font-wordmark text-5xl leading-none tracking-[-0.03em]">
            Leno
          </span>
        </div>
        <p className="text-balance text-muted-foreground">
          Note down everything on your mind, out loud, without worrying about
          where it goes. Leno listens, understands, classifies, and
          automatically connects your ideas through a multi-agent AI
          architecture.
        </p>
      </header>

      <NotesBoard />
    </div>
  )
}
