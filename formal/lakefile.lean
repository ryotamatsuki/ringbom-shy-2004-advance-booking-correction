import Lake
open Lake DSL

package ringbomShyCorrection where

require mathlib from git "https://github.com/leanprover-community/mathlib4.git" @ "v4.34.0"

lean_lib RingbomShy where
  roots := #[`RingbomShy]
