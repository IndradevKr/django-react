import axios from "axios";

const getBlogsList = async (params?: Record<string, unknown>) => {
  const response = await axios.get("http://localhost:8000/blogs/list/", {
    params,
  });
  return response.data;
};

export { getBlogsList };
