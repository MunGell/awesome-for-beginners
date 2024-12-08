import { Sponsor } from "../types";

interface FooterProps {
  sponsors: Sponsor[];
}

export default function Footer({ sponsors }: FooterProps) {
  return (
    <footer className="bg-gray-800 py-8">
      <div className="container mx-auto px-4">
        <h2 className="text-2xl font-semibold mb-4">Sponsors</h2>
        <div className="flex flex-wrap gap-4">
          {sponsors.map((sponsor) => (
            <a
              key={sponsor.name}
              href={sponsor.link}
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center space-x-2 bg-gray-700 rounded-full p-2 hover:bg-gray-600 transition-colors"
            >
              <img
                src={sponsor.image}
                alt={sponsor.name}
                className="w-8 h-8 rounded-full"
              />
              <span>{sponsor.name}</span>
            </a>
          ))}
        </div>
      </div>
    </footer>
  );
}
