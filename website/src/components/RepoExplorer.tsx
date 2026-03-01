"use client";

import { useState, useMemo } from "react";
import { Data } from "@/types/data";
import SearchBar from "./SearchBar";
import TechFilter from "./TechFilter";
import RepoCard from "./RepoCard";
import SponsorBadge from "./SponsorBadge";

interface RepoExplorerProps {
  data: Data;
}

export default function RepoExplorer({ data }: RepoExplorerProps) {
  const [search, setSearch] = useState("");
  const [selectedTech, setSelectedTech] = useState<string | null>(null);

  const allTechnologies = useMemo(() => {
    const techSet = new Set<string>();
    data.repositories.forEach((repo) =>
      repo.technologies.forEach((t) => techSet.add(t))
    );
    return Array.from(techSet).sort();
  }, [data.repositories]);

  const filteredRepos = useMemo(() => {
    const query = search.toLowerCase().trim();
    return data.repositories.filter((repo) => {
      const matchesSearch =
        !query ||
        repo.name.toLowerCase().includes(query) ||
        repo.description.toLowerCase().includes(query) ||
        repo.technologies.some((t) => t.toLowerCase().includes(query));

      const matchesTech =
        !selectedTech || repo.technologies.includes(selectedTech);

      return matchesSearch && matchesTech;
    });
  }, [data.repositories, search, selectedTech]);

  return (
    <div className="mx-auto max-w-6xl px-4 py-8 sm:px-6 lg:px-8">
      {/* Header */}
      <header className="mb-10 text-center">
        <h1 className="text-3xl font-bold tracking-tight text-foreground sm:text-4xl">
          Awesome First PR Opportunities
        </h1>
        <p className="mt-3 text-base text-muted max-w-2xl mx-auto">
          A curated list of awesome beginners-friendly projects. Find your next
          open source contribution!
        </p>

        {/* Sponsors */}
        {data.sponsors.length > 0 && (
          <div className="mt-6 flex flex-wrap items-center justify-center gap-3">
            <span className="text-xs font-medium uppercase tracking-wider text-muted">
              Sponsors
            </span>
            {data.sponsors.map((sponsor) => (
              <SponsorBadge key={sponsor.name} sponsor={sponsor} />
            ))}
          </div>
        )}
      </header>

      {/* Search and Filter */}
      <div className="mb-8 space-y-4">
        <div className="flex flex-col items-center gap-4 sm:flex-row">
          <SearchBar value={search} onChange={setSearch} />
          <div className="text-sm text-muted whitespace-nowrap">
            {filteredRepos.length}{" "}
            {filteredRepos.length === 1 ? "project" : "projects"}
          </div>
        </div>
        <TechFilter
          technologies={allTechnologies}
          selected={selectedTech}
          onSelect={setSelectedTech}
        />
      </div>

      {/* Results */}
      {filteredRepos.length > 0 ? (
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {filteredRepos.map((repo) => (
            <RepoCard key={repo.name} repo={repo} />
          ))}
        </div>
      ) : (
        <div className="flex flex-col items-center justify-center py-20 text-center">
          <svg
            className="h-12 w-12 text-muted/40"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={1.5}
              d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
          <p className="mt-4 text-lg font-medium text-foreground">
            No projects found
          </p>
          <p className="mt-1 text-sm text-muted">
            Try adjusting your search or filters
          </p>
        </div>
      )}

      {/* Footer */}
      <footer className="mt-16 border-t border-card-border pt-8 text-center text-sm text-muted">
        <p>
          Data sourced from{" "}
          <a
            href="https://github.com/MunGell/awesome-for-beginners"
            target="_blank"
            rel="noopener noreferrer"
            className="font-medium text-accent hover:underline"
          >
            awesome-for-beginners
          </a>
          . Contributions welcome!
        </p>
      </footer>
    </div>
  );
}
