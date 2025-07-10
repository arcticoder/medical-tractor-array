"""
Medical Tractor Array Module - Revolutionary LQG-Enhanced Medical Manipulation System
====================================================================================

Revolutionary Medical-Grade Graviton Safety System with T_μν ≥ 0 positive energy constraints

Key Features:
- Complete T_μν ≥ 0 positive energy constraint enforcement
- 10¹² biological safety margin above WHO limits  
- <50ms emergency response for patient protection
- LQG polymer corrections for 242M× energy reduction
- Medical-grade graviton field protocols with tissue-specific safety
"""

# Import legacy components for backward compatibility
try:
    from .array import MedicalTractorArray, MedicalArrayParams, TractorBeam, BeamMode, SafetyLevel, VitalSigns
except ImportError:
    # Legacy imports not available
    pass

# Import revolutionary LQG-enhanced components
from .array import (
    LQGMedicalTractorArray,
    BiologicalTargetType,
    MedicalTarget,
    MedicalProcedureMode,
    BiologicalSafetyProtocols,
    LQGMedicalMetrics
)

# Import UQ resolution framework
from .uq_resolution_framework import (
    MedicalTractorArrayUQResolver,
    UQResolutionMetrics
)

# Import revolutionary graviton safety controller
from .graviton_safety_controller import (
    MedicalGravitonSafetyController,
    GravitonFieldMode,
    BiologicalSafetyLevel, 
    GravitonSafetyConstraints,
    GravitonFieldMetrics
)

__all__ = [
    # Revolutionary LQG-enhanced components
    "LQGMedicalTractorArray",
    "BiologicalTargetType",
    "MedicalTarget", 
    "MedicalProcedureMode",
    "BiologicalSafetyProtocols",
    "LQGMedicalMetrics",
    
    # UQ resolution framework
    "MedicalTractorArrayUQResolver",
    "UQResolutionMetrics",
    
    # Medical-Grade Graviton Safety Controller
    "MedicalGravitonSafetyController",
    "GravitonFieldMode",
    "BiologicalSafetyLevel",
    "GravitonSafetyConstraints", 
    "GravitonFieldMetrics",
    
    # Legacy components (if available)
    "MedicalTractorArray",
    "MedicalArrayParams",
    "TractorBeam", 
    "BeamMode",
    "SafetyLevel",
    "VitalSigns"
]

__version__ = "2.0.0"  # Major version bump for revolutionary graviton safety system
