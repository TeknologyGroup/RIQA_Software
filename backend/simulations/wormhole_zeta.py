import numpy as np
from mpmath import zetazero
from scipy.signal import hilbert, find_peaks
from scipy.stats import ks_2samp, ttest_ind
from sklearn.preprocessing import StandardScaler
import pandas as pd
import json

class UnifiedSimulation:
    def __init__(self, zero_index=1, r_range=10, points=100, beta=10, gamma=1):
        self.zero_index = zero_index
        self.r_range = r_range
        self.points = points
        self.beta = beta
        self.gamma = gamma
        self.t_n = float(zetazero(zero_index).imag)
        self.b0 = self.t_n

    def wormhole_metric(self):
        """Calcola la metrica del wormhole."""
        r = np.linspace(self.b0, self.b0 + self.r_range, self.points)
        b_r = self.b0 * np.ones_like(r)
        Phi_r = -self.b0 / r
        g_rr = 1 / (1 - b_r / r)
        return {'r': r.tolist(), 'b_r': b_r.tolist(), 'Phi_r': Phi_r.tolist(), 'g_rr': g_rr.tolist(), 'b0': self.b0}

    def preprocess_signal(self, signal, fs=12000):
        """Preprocessing avanzato per Quantum Chaos Fingerprinting."""
        signal = signal - np.mean(signal)
        scaler = StandardScaler()
        signal_scaled = scaler.fit_transform(signal.reshape(-1, 1)).flatten()
        analytic_signal = hilbert(signal_scaled)
        return np.abs(analytic_signal)

    def harmonic_analysis(self, signal, fs=12000, harmonics=3):
        """Analisi armoniche per rilevare frequenze critiche."""
        n = len(signal)
        fft = np.fft.fft(signal)
        freqs = np.fft.fftfreq(n, 1/fs)
        fft_magnitude = np.abs(fft)[:n//2]
        freqs_positive = freqs[:n//2]
        peaks, _ = find_peaks(fft_magnitude, height=np.max(fft_magnitude)*0.1, distance=10)
        return freqs_positive[peaks][:harmonics].tolist()

    def quantum_chaos_metric(self, detected_freqs, theoretical_freq):
        """Metrica critica C per Quantum Chaos Fingerprinting."""
        z_zeros = [float(zetazero(i).imag) for i in range(1, 11)]
        f_scaled = [f / theoretical_freq * self.b0 for f in detected_freqs]
        correlations = [1 / (1 + self.beta * abs(f - min(z_zeros, key=lambda z: abs(z - f))))**self.gamma 
                        for f in f_scaled]
        return correlations, f_scaled, z_zeros

    def statistical_tests(self, normal_corrs, fault_corrs):
        """Test statistici robusti."""
        ks_stat, ks_pvalue = ks_2samp(normal_corrs, fault_corrs)
        t_stat, t_pvalue = ttest_ind(normal_corrs, fault_corrs, equal_var=False)
        ci_normal = np.percentile([np.mean(np.random.choice(normal_corrs, len(normal_corrs))) for _ in range(1000)], [2.5, 97.5])
        ci_fault = np.percentile([np.mean(np.random.choice(fault_corrs, len(fault_corrs))) for _ in range(1000)], [2.5, 97.5])
        return {'ks_pvalue': ks_pvalue, 't_pvalue': t_pvalue, 'ci_normal': ci_normal.tolist(), 'ci_fault': ci_fault.tolist()}

def simulate_cwru_data(file_key, rpm, fault_type, fs=12000, duration=1):
    """Simula segnali CWRU per Quantum Chaos Fingerprinting."""
    t = np.linspace(0, duration, int(fs * duration))
    base_freq = 159.8 * (rpm / 1797)  # BPFI scalato
    if "normal" in file_key:
        return np.random.normal(0, 0.1, len(t)) + 0.5 * np.sin(2 * np.pi * base_freq * t)
    else:
        return 1.0 * np.sin(2 * np.pi * base_freq * t) + 0.3 * np.sin(2 * np.pi * 2 * base_freq * t) + np.random.normal(0, 0.05, len(t))

def run_unified_analysis():
    files = ["normal_1797", "normal_1772", "normal_1750", "normal_1730", 
             "ir_007_1797", "ir_007_1772", "ir_007_1750", "ir_007_1730", 
             "ir_014_1797", "ir_014_1772", "ir_014_1750", "ir_014_1730"]
    sim = UnifiedSimulation(zero_index=1, beta=10, gamma=1)
    theoretical_freq = 159.8
    results, normal_corrs, fault_corrs = [], [], []
    
    for file_key in files:
        rpm = int(file_key.split('_')[-1])
        fault_type = "BPFI" if "ir" in file_key else "None"
        signal = simulate_cwru_data(file_key, rpm, fault_type)
        envelope = sim.preprocess_signal(signal)
        detected_freqs = sim.harmonic_analysis(envelope)
        corrs, f_scaled, z_zeros = sim.quantum_chaos_metric(detected_freqs, theoretical_freq)
        
        for i, (freq, corr) in enumerate(zip(detected_freqs[:3], corrs[:3])):
            harmonic = f"H{i+1}"
            error = abs(freq - theoretical_freq * (rpm / 1797)) / (theoretical_freq * (rpm / 1797)) * 100
            critical = "Yes" if corr > 0.7 else "No"
            nearest_zero = min(z_zeros, key=lambda z: abs(z - f_scaled[i]))
            results.append({
                "File Key": file_key, "Condition": "inner_race" if "ir" in file_key else "normal",
                "RPM": rpm, "Fault Type": fault_type, "Harmonic": harmonic,
                "Detected Freq": freq, "Theoretical Freq": theoretical_freq * (rpm / 1797),
                "Error %": error, "Correlation": corr, "Nearest Zero": nearest_zero, "Critical": critical
            })
            if "normal" in file_key:
                normal_corrs.append(corr)
            else:
                fault_corrs.append(corr)
    
    stats = sim.statistical_tests(normal_corrs, fault_corrs)
    df = pd.DataFrame(results)
    df.to_csv("validation_summary_6205.csv", index=False)
    with open("validation_stats.json", "w") as f:
        json.dump(stats, f)
    return df, stats

if __name__ == "__main__":
    df, stats = run_unified_analysis()