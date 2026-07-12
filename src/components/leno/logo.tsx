import Image from "next/image"
import { cn } from "@/lib/utils"

export function Logo({ className }: { className?: string }) {
  return (
    <span
      className={cn(
        "inline-flex h-9 w-9 shrink-0 items-center justify-center overflow-hidden rounded-full bg-white",
        className,
      )}
    >
      <Image src="/logo.png" alt="Leno logo" width={112} height={101} className="h-7 w-auto" priority />
    </span>
  )
}
