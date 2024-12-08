import { Button } from "@/components/ui/button";

interface FilterBarProps {
  technologies: string[];
  selectedTech: string | null;
  onSelectTech: (tech: string | null) => void;
}

export default function FilterBar({
  technologies,
  selectedTech,
  onSelectTech,
}: FilterBarProps) {
  return (
    <div className="mb-8">
      <h2 className="text-2xl font-semibold mb-4">Filter by Technology</h2>
      <div className="flex flex-wrap gap-2">
        <Button
          variant={selectedTech === null ? "default" : "secondary"}
          onClick={() => onSelectTech(null)}
        >
          All
        </Button>
        {technologies.map((tech) => (
          <Button
            key={tech}
            variant={selectedTech === tech ? "default" : "secondary"}
            onClick={() => onSelectTech(tech)}
          >
            {tech}
          </Button>
        ))}
      </div>
    </div>
  );
}
