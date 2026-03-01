export interface Sponsor {
  name: string;
  image: string;
  link: string;
}

export interface Repository {
  name: string;
  link: string;
  label?: string;
  technologies: string[];
  description: string;
}

export interface Data {
  sponsors: Sponsor[];
  technologies: Record<string, string>;
  repositories: Repository[];
}
