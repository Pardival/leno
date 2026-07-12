import { cn } from "@/lib/utils"

export function Logo({ className }: { className?: string }) {
  return (
    <svg
      viewBox="0 0 200 200"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      className={cn("h-9 w-9", className)}
      role="img"
      aria-label="Leno logo"
    >
      <path
        d="M97 21C118 15 143 22 160 39C177 56 187 80 184 103C181 128 168 151 145 164C123 177 94 180 70 171C46 162 28 143 22 118C16 94 20 67 37 49C52 33 76 27 97 21Z"
        fill="#F4EFE6"
        stroke="#141414"
        strokeWidth="9"
        strokeLinejoin="round"
        strokeLinecap="round"
      />
      <circle cx="82" cy="111" r="7.5" fill="#141414" />
      <circle cx="118" cy="108" r="7.5" fill="#141414" />
    </svg>
  )
}
