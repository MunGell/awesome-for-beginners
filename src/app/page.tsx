"use client";

import { useState } from "react";
import Header from "./components/Header";
import FilterBar from "./components/FilterBar";
import ProjectGrid from "./components/ProjectGrid";
import Footer from "./components/Footer";
import { Project, Sponsor, Technology } from "./types";

// Import the data from the provided JSON
import data from "../../data.json";

export default function Home() {
  const [selectedTech, setSelectedTech] = useState<string | null>(null);

  const filteredProjects = selectedTech
    ? data.repositories.filter((project) =>
        project.technologies.includes(selectedTech)
      )
    : data.repositories;

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <Header title="Awesome Open Source Projects" />
      <main className="container mx-auto px-4 py-8">
        <FilterBar
          technologies={Object.keys(data.technologies)}
          selectedTech={selectedTech}
          onSelectTech={setSelectedTech}
        />
        <ProjectGrid projects={filteredProjects} />
      </main>
      {/* <Footer sponsors={data.sponsors} /> */}
    </div>
  );
}
