export interface Sponsor {
  name: string;
  image: string;
  link: string;
}

export interface Technology {
  [key: string]: string;
}

export interface Project {
  name: string;
  link: string;
  label: string | undefined;
  technologies: string[];
  description: string;
}

export interface Data {
  sponsors: Sponsor[];
  technologies: Technology;
  repositories: Project[];
}
