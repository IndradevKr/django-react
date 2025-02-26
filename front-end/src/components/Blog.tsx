interface IProps {
  title: string;
  content: string;
}

const Blog = ({ title, content }: IProps) => {
  return (
    <>
      <h3>{title}</h3>
      <br />
      <p>{content}</p>
    </>
  );
};
export default Blog;
