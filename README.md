# Using Rust Functions in Python Shiny

## Setup
Both Python and Rust have to be installed.

```bash
python -m venv .env
source .env/bin/activate
pip install maturin shiny
maturin develop
shiny run
```

If you change Rust code, then you have to run `maturin develop` again.

## References
- [Python Shiny](https://shiny.rstudio.com/py/)
- [PyO3](https://pyo3.rs/v0.16.4/)
