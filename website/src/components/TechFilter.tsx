"use client";

interface TechFilterProps {
  technologies: string[];
  selected: string | null;
  onSelect: (tech: string | null) => void;
}

export default function TechFilter({
  technologies,
  selected,
  onSelect,
}: TechFilterProps) {
  return (
    <div className="flex flex-wrap gap-2">
      <button
        onClick={() => onSelect(null)}
        className={`rounded-full px-3 py-1.5 text-xs font-medium transition-all cursor-pointer ${
          selected === null
            ? "bg-accent text-white shadow-sm"
            : "bg-tag-bg text-tag-text hover:bg-accent-light hover:text-accent"
        }`}
      >
        All
      </button>
      {technologies.map((tech) => (
        <button
          key={tech}
          onClick={() => onSelect(selected === tech ? null : tech)}
          className={`rounded-full px-3 py-1.5 text-xs font-medium transition-all cursor-pointer ${
            selected === tech
              ? "bg-accent text-white shadow-sm"
              : "bg-tag-bg text-tag-text hover:bg-accent-light hover:text-accent"
          }`}
        >
          {tech}
        </button>
      ))}
    </div>
  );
}
