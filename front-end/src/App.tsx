import { useEffect, useState } from "react";
import "./App.css";
import { getBlogsList } from "./api/blog.api";
import Blog from "./components/Blog";

interface IBlog {
  id: string;
  title: string;
  content: string;
}

function App() {
  const [blogs, setBlogs] = useState([]);

  useEffect(() => {
    const res = getBlogsList();
    res.then((data) => {
      setBlogs(data);
    });
  }, []);

  return (
    <>
      {blogs.length
        ? blogs.map((blog: IBlog) => (
            <Blog key={blog?.id} title={blog?.title} content={blog?.content} />
          ))
        : null}
    </>
  );
}

export default App;
