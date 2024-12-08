import { Github } from "lucide-react";

interface HeaderProps {
  title: string;
}

export default function Header({ title }: HeaderProps) {
  return (
    <header className="bg-gray-800 py-6">
      <div className="container mx-auto px-4 flex items-center justify-between">
        <h1 className="text-4xl font-bold">{title}</h1>
        <a
          href="https://github.com"
          target="_blank"
          rel="noopener noreferrer"
          className="text-gray-300 hover:text-white transition-colors"
        >
          <Github size={32} />
        </a>
      </div>
    </header>
  );
}
