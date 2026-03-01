import { Sponsor } from "@/types/data";

interface SponsorBadgeProps {
  sponsor: Sponsor;
}

export default function SponsorBadge({ sponsor }: SponsorBadgeProps) {
  return (
    <a
      href={sponsor.link}
      target="_blank"
      rel="noopener noreferrer"
      className="inline-flex items-center gap-2 rounded-full border border-card-border bg-card-bg px-3 py-1.5 text-sm font-medium text-foreground transition-all hover:border-accent/40 hover:shadow-sm"
    >
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img
        src={sponsor.image}
        alt={sponsor.name}
        width={24}
        height={24}
        className="rounded-full"
      />
      {sponsor.name}
    </a>
  );
}
