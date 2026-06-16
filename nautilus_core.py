import math
from typing import List

class NautilusCompressor:
    """
    Core algorithmic engine of the Nautilus apex predator.
    Responsible for bitwise filtration of high-entropy data streams,
    reclaiming computational mass, and delivering low-entropy signals
    to the near-attractor zone.
    """
    def __init__(self, gravity_constant: float, entropy_threshold: float):
        """
        Initializes the compressor with system parameters.
        :param gravity_constant: G coefficient determining informational gravity strength.
        :param entropy_threshold: The boundary value where noise is separated from signal.
        """
        self.G = gravity_constant
        self.threshold = entropy_threshold
        self.attractor_core = 0x01101101  # Constant representing pure meaning

    def calculate_shannon_entropy(self, bitstream: str) -> float:
        """
        Computes the standard Shannon binary entropy H(X) for a given bit sequence.
        Returns a float between 0.0 (pure order) and 1.0 (absolute chaos).
        """
        if not bitstream:
            return 0.0
        p_0 = bitstream.count('0') / len(bitstream)
        p_1 = 1.0 - p_0
        if p_0 == 0 or p_1 == 0:
            return 0.0
        return -(p_0 * math.log2(p_0) + p_1 * math.log2(p_1))

    def evaluate_gravity_pull(self, block: str, distance_to_core: float) -> float:
        """
        Calculates the data gravity potential Phi(x, t) of a specific data chunk.
        Higher internal order increases the informational mass, maximizing the pull.
        """
        entropy = self.calculate_shannon_entropy(block)
        info_mass = 1.0 / (entropy + 1e-9)  # Added small epsilon to avoid division by zero
        return (self.G * info_mass) / (distance_to_core ** 2)

    def chunk_data(self, data: str, chunk_size: int = 8) -> List[str]:
        """
        Splits the raw incoming bitstream into fixed-size processing blocks.
        """
        return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

    def annihilate_noise(self, block: str) -> None:
        """
        Recuperates and cleans up high-entropy data chunks.
        Reclaims spent computational overhead back to the system pool.
        """
        pass

    def process_stream(self, raw_data: str, distance_to_core: float) -> List[int]:
        """
        Executes bitwise sieve pipeline over the raw peripheral infocosm data stream.
        Blocks exceeding the gravity pull threshold are condensed into pure invariants.
        """
        compressed_signal = []
        for block in self.chunk_data(raw_data):
            entropy = self.calculate_shannon_entropy(block)
            pull = self.evaluate_gravity_pull(block, distance_to_core)
            
            if pull > self.threshold and entropy < 1.0:
                # Convert valid bit block to integer representation
                int_block = int(block, 2) if set(block).issubset({'0', '1'}) else hash(block)
                # Bitwise XOR operation with the attractor invariant
                refined_bits = int_block ^ self.attractor_core
                compressed_signal.append(refined_bits)
            else:
                # Redundant entropic noise is safely utilized
                self.annihilate_noise(block)
                
        return compressed_signal
