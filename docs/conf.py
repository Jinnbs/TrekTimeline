# Book settings
# Learn more at https://jupyterbook.org/customize/config.html
# Comprehensive example: https://github.com/executablebooks/jupyter-book/blob/master/docs/_config.yml

title: Example Jupyter Book for Read the Docs
author: Read the Docs team
logo: logo.png

# Force re-execution of notebooks on each build.
# See https://jupyterbook.org/content/execute.html
execute:
  execute_notebooks: force

# Define the name of the latex output file for PDF builds
latex:
  latex_documents:
    targetname: book.tex

# Add a bibtex file so that we can create citations
bibtex_bibfiles:
  - references.bib

# Information about where the book exists on the web
repository:
  url: https://github.com/readthedocs-examples/example-jupyter-book  # Online location of your book
  path_to_book: docs  # Optional path to your book, relative to the repository root
  branch: main  # Which branch of the repository should be used when creating links (optional)

# Add GitHub buttons to your book
# See https://jupyterbook.org/customize/config.html#add-a-link-to-your-repository
html:
  use_issues_button: true
  use_repository_button: true

sphinx:
  config:
    intersphinx_mapping:
      ebp:
        - "https://executablebooks.org/en/latest/"
        - null
      myst-parser:
        - "https://myst-parser.readthedocs.io/en/latest/"
        - null
      myst-nb:
        - "https://myst-nb.readthedocs.io/en/latest/"
        - null
      sphinx:
        - "https://www.sphinx-doc.org/en/master"
        - null
      nbformat:
        - "https://nbformat.readthedocs.io/en/latest"
        - null
      sd:
        - "https://sphinx-design.readthedocs.io/en/latest"
        - null
      sphinxproof:
        - "https://sphinx-proof.readthedocs.io/en/latest/"
        - null
    hoverxref_intersphinx:
     - "sphinxproof"
    mathjax3_config:
      tex:
        macros:
          "N": "\\mathbb{N}"
          "floor": ["\\lfloor#1\\rfloor", 1]
          "bmat": ["\\left[\\begin{array}"]
          "emat": ["\\end{array}\\right]"]
        
  extra_extensions:
    - sphinx.ext.intersphinx
    - sphinx_inline_tabs
    - sphinx_proof
    - sphinx_examples
    - hoverxref.extension
