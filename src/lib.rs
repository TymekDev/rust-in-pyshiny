use pyo3::prelude::*;

#[pyfunction]
fn hello_rust() -> PyResult<String> {
    Ok("Hello from Rust!".to_string())
}

#[pyfunction]
fn calc_in_rust(x: i32) -> PyResult<i32> {
    Ok(x * 2 + 2)
}

#[pymodule]
fn pyshiny_rust_lib(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(hello_rust, m)?)?;
    m.add_function(wrap_pyfunction!(calc_in_rust, m)?)?;
    Ok(())
}
