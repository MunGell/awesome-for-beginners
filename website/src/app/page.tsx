import RepoExplorer from "@/components/RepoExplorer";
import data from "../../../data.json";
import { Data } from "@/types/data";

export default function Home() {
  return <RepoExplorer data={data as Data} />;
}
