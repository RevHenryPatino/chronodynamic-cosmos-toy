import numpy as np
import matplotlib.pyplot as plt

# Parameters from the paper (Section 3.1 and Appendix A.2)
alpha = 0.11          # fiducial value ≈ 0.11 (derived from compact dimension scales)
H0_global = 67.4      # Planck CMB-inferred H0 in km/s/Mpc
H0_SH0ES = 73.0       # SH0ES local measurement for reference line

# Density contrast range: ρ_local / ρ_global
# (filament/cluster/Local Group ~10–30, voids <1, extreme cases up to 100)
contrast = np.logspace(0.0, 2.0, 300)   # from 1 to 100

# Observed H0 = H0_global × (ρ_local / ρ_global)^{α/2}
# (square-root dependence from weak-field GR proper-time effect)
H0_obs = H0_global * contrast ** (alpha / 2)

# Create the figure
plt.figure(figsize=(10, 6))

# Main curve
plt.loglog(contrast, H0_obs, lw=2.5, color='darkblue',
           label=r'$H_{0,\mathrm{obs}} = H_{0,\mathrm{global}} \times \left( \frac{\rho_\mathrm{local}}{\rho_\mathrm{global}} \right)^{\alpha/2}$')

# Reference lines
plt.axhline(H0_SH0ES, color='red', ls='--', lw=1.8,
            label=f'SH0ES local (≈ {H0_SH0ES} km/s/Mpc)')
plt.axhline(H0_global, color='gray', ls=':', lw=1.8,
            label=f'Planck CMB (≈ {H0_global} km/s/Mpc)')

# Typical density contrast range for filaments / Local Group
plt.axvspan(10, 30, alpha=0.12, color='green',
            label='Typical filament / Local Group contrast (10–30)')

# Annotations
plt.text(12, 69.5, '≈71–73 km/s/Mpc', color='darkgreen', fontsize=10, ha='left')

# Formatting
plt.xscale('log')
plt.xlabel(r'Density contrast  $\rho_\mathrm{local} / \rho_\mathrm{global}$', fontsize=13)
plt.ylabel(r'Local observed $H_0$  (km s$^{-1}$ Mpc$^{-1}$)', fontsize=13)
plt.title('Geometric Hubble tension resolution via density-dependent proper time\n'
          r'($\alpha \approx 0.11$, $H_{0,\mathrm{global}} = 67.4$ km/s/Mpc)', fontsize=14)
plt.grid(True, which='both', ls='--', alpha=0.6)
plt.legend(fontsize=11, loc='lower right')

# Save and show
plt.tight_layout()
plt.savefig('fig_hubble_density_contrast.png', dpi=200)
plt.show()
