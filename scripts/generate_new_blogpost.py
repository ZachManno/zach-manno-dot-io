#!/usr/bin/env python3
"""
    USAGE:
        - With the default directories for this repo
        generate_new_blogpost.py --post-date 2022-03-27 --post-title "Generating A New Blogpost"
        - With custom directories
        generate_new_blogpost.py ./path/to/static/content-dir ./path/to/blogpost-dir --post-date 2022-03-27 --post-title "Generating A New Blogpost"
"""
import argparse
import shutil
from pathlib import Path
from datetime import datetime
from shutil import copyfile


class BlogPostGenerator:
    """
    Create a new JSON Handbrake config file for a folder tree of files
    using specific settings for high efficiency encoding.
    If DIR_OUT option is used and is different than DIR then all non-encoded files are
    first copied to the encoded files dir.
    -
    Resolutions can now be set to auto or auto-half - this requires ffprobe to be
    installed on your system - and will automatically set the resolutions based on the
    original video, or in case of auto-half to half the size of it (half width and height).
    Note that using this option will slow down the process as every video file will be checked.
    """

    BLOG_HTML_TEMPLATE = \
        """
                <div class="col-md-6 mb-4">
                    <div class="card mb-4 h-100">
                        <a href="#!"><img class="card-img-top" src="assets/{BLOGPOST_FILENAME}/{BLOG_IMAGE}"
                                          alt="..."/></a>
                        <div class="card-body">
                            <div class="small text-muted">{HUMAN_READABLE_DATE}</div>
                            <h2 class="card-title">{POST_TITLE}</h2>
                        <!-- TODO: Edit this card text if you wish to elaborate -->
                            <p class="card-text">{POST_TITLE}
                                </p>
                            <a class="btn btn-primary" href="blogposts/{FULL_BLOGPOST_FILENAME}">Read more →</a>
                        </div>
                    </div>
                </div>
    """

    def __init__(self):
        p = argparse.ArgumentParser(description=self.__doc__)
        p.add_argument(
            "static_content_dir",
            nargs="?",
            default=Path("../zachmanno.io/static/"),
            type=Path,
            help="Path of static content. Default: ../zachmanno.io/static/",
        )
        p.add_argument(
            "blogposts_content_dir",
            nargs="?",
            default=Path("../zachmanno.io/static/blogposts/"),
            type=Path,
            help="Path of blogposts directory. Default: ../zachmanno.io/static/blogposts/",
        )
        p.add_argument(
            "--post-date",
            nargs="?",
            type=str,
            default=None,
            help="Date of blogpost in yyyy-mm-dd format",
        )
        p.add_argument(
            "--post-title",
            nargs="?",
            type=str,
            default=None,
            help="Name of blogpost",
        )
        p.add_argument(
            "--post-header-image",
            nargs="?",
            type=str,
            default=None,
            help="Path to the image to be used in this blog (make sure around 2x1 LxW ratio)",
        )
        self.args = p.parse_args()
        self.static_content_dir = self.args.static_content_dir
        self.blogposts_content_dir = self.args.blogposts_content_dir
        self.post_title = self.args.post_title
        self.post_date = self.args.post_date
        self.post_header_image = self.args.post_header_image
        self.create_blogpost()

    def create_blogpost(self):
        # sys.exit(0)
        print(f'Writing new blog to '
              f'static content dir: {self.static_content_dir}, '
              f'blogpost dir: {self.blogposts_content_dir}, '
              f'with post title: {self.post_title}, '
              f'post date: {self.post_date}')
        python_date = datetime.strptime(self.post_date, '%Y-%m-%d')
        blogpost_filename = f'blogpost-{python_date.strftime("%b-%d-%Y").lower()}.html'
        self.create_blogfile_from_template(self.blogposts_content_dir / blogpost_filename)
        self.edit_index_and_blog_files(blogpost_filename, self.static_content_dir / 'blog.html',
                                       self.static_content_dir / 'index.html')

    def edit_index_and_blog_files(self, blogpost_filename, blog_html_file, index_html_file):
        human_readable_date = datetime.strptime(self.post_date, '%Y-%m-%d').strftime('%B %d, %Y')
        search_and_replace_dict = {
            '{POST_TITLE}': self.post_title,
            '{HUMAN_READABLE_DATE}': human_readable_date,
            '{BLOGPOST_FILENAME}': blogpost_filename.replace('.html', ''),
            '{FULL_BLOGPOST_FILENAME}': blogpost_filename,
            '{BLOG_IMAGE}': self.post_header_image
        }
        html_text = BlogPostGenerator.BLOG_HTML_TEMPLATE
        for search_term, replace_term in search_and_replace_dict.items():
            html_text = html_text.replace(search_term, replace_term)
        print(html_text)
        lines_to_insert = []
        for insert_html_line in html_text.split("\n"):
            lines_to_insert.append(insert_html_line + '\n')
        blog_html_lines = []

        # Insert for blog.html
        with blog_html_file.open("r", encoding="utf-8") as new_blogpost_file:
            blog_html_lines = new_blogpost_file.readlines()
            idx_at_which_to_insert = 0
            for idx, line in enumerate(blog_html_lines):
                # Find the row with blogPostRow ID, insert the new blog at the top
                if 'blogPostRow' in line:
                    idx_at_which_to_insert = idx + 1
            blog_html_lines[idx_at_which_to_insert:2] = lines_to_insert
        with blog_html_file.open("w", encoding="utf-8") as new_blogpost_file:
            for line in blog_html_lines:
                new_blogpost_file.write(line)

        # Insert for index.html
        with index_html_file.open("r", encoding="utf-8") as new_index_file:
            index_html_lines = new_index_file.readlines()
            idx_at_which_to_insert = 0
            for idx, line in enumerate(index_html_lines):
                # Find the row with blogPostRow ID, insert the new blog at the top
                if 'blogPostRow' in line:
                    idx_at_which_to_insert = idx + 1
            index_html_lines[idx_at_which_to_insert:2] = lines_to_insert
        with index_html_file.open("w", encoding="utf-8") as new_index_file:
            for line in index_html_lines:
                new_index_file.write(line)


    def create_blogfile_from_template(self, blogpost_file):
        human_readable_date = datetime.strptime(self.post_date, '%Y-%m-%d').strftime('%B %d, %Y')
        search_and_replace_dict = {
            '{POST_TITLE}': self.post_title,
            '{HUMAN_READABLE_DATE}': human_readable_date,
            '{BLOGPOST_FILENAME}': blogpost_file.name.replace('.html', ''),
            '{BLOG_IMAGE}': self.post_header_image
        }
        copyfile('./blogpost-templates/new-post-template.html', blogpost_file)
        p = Path(self.static_content_dir / 'assets' / blogpost_file.name.replace(".html", ""))
        print(f'Moved the image {self.post_header_image} to the directory {p}')
        p.mkdir(parents=True, exist_ok=True)
        shutil.move(self.post_header_image, p / self.post_header_image)
        with blogpost_file.open("r", encoding="utf-8") as new_blogpost_file:
            file_data = new_blogpost_file.read()
            for search_term, replace_term in search_and_replace_dict.items():
                file_data = file_data.replace(search_term, replace_term)

        with blogpost_file.open("w", encoding="utf-8") as new_blogpost_file:
            new_blogpost_file.write(file_data)


if __name__ == "__main__":
    BlogPostGenerator()
