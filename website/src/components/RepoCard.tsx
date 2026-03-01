import { Repository } from "@/types/data";

interface RepoCardProps {
  repo: Repository;
}

export default function RepoCard({ repo }: RepoCardProps) {
  return (
    <a
      href={repo.link}
      target="_blank"
      rel="noopener noreferrer"
      className="group block rounded-xl border border-card-border bg-card-bg p-5 transition-all hover:border-accent/40 hover:shadow-md hover:shadow-accent/5"
    >
      <div className="flex items-start justify-between gap-3">
        <h3 className="text-base font-semibold text-foreground group-hover:text-accent transition-colors">
          {repo.name}
        </h3>
        <svg
          className="mt-0.5 h-4 w-4 shrink-0 text-muted opacity-0 transition-all group-hover:opacity-100 group-hover:translate-x-0.5"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
          />
        </svg>
      </div>

      <p className="mt-2 text-sm leading-relaxed text-muted line-clamp-2">
        {repo.description}
      </p>

      <div className="mt-4 flex flex-wrap items-center gap-2">
        {repo.technologies.map((tech) => (
          <span
            key={tech}
            className="inline-flex items-center rounded-md bg-accent-light px-2 py-0.5 text-xs font-medium text-accent"
          >
            {tech}
          </span>
        ))}
        {repo.label && (
          <span className="inline-flex items-center rounded-md bg-tag-bg px-2 py-0.5 text-xs text-tag-text">
            {repo.label}
          </span>
        )}
      </div>
    </a>
  );
}
