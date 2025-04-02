# API Reference
## `fresnel.calculate_fresnel()`
- **Description**: Computes ∫₀^∞ sin(x²) dx.
- **Returns**: Tuple `(result: float, error: float)`.

## `dirac_delta.curved_dirac_delta()`
- **Description**: Computes ∫δ(x²−1)√(1+x²) dx.
- **Returns**: Approximated value of √2.

## `quantum_path.quantum_path_simulation()`
- **Parameters**: 
  - `num_paths`: Number of quantum paths (default=100).
  - `num_curvets`: Resolution of each path (default=1000).
- **Returns**: Complex path integral result.
