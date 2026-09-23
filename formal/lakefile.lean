import Lake
open Lake DSL

package ringbomShyCorrection where

require "leanprover-community" / "mathlib4" @ git "v4.34.0"

@[default_target]
lean_lib RingbomShy where
  roots := #[`RingbomShy]
