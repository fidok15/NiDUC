import pandas as pd
import matplotlib.pyplot as plt

def plot_comparison(df):
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # Poprawność nc
    line1, = axes[0].plot(df['current_error'], df['maj_nc'], label='Większościowy', linewidth=4, markersize=8, alpha = 0.8)
    line2, = axes[0].plot(df['current_error'], df['wt_nc'], label='Wagowy', linewidth=2, markersize=6, alpha = 0.8)
    line3, = axes[0].plot(df['current_error'], df['sm_nc'], label='Wygładzający', linewidth=2, markersize=6, alpha = 0.8)
    
    mid_idx = len(df) // 2
    axes[0].text(df['current_error'].iloc[mid_idx + 25], df['maj_nc'].iloc[mid_idx], 
                 'MAJ', fontsize=10, fontweight='bold', 
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=line1.get_color(), alpha=0.7, edgecolor='none'))
    axes[0].text(df['current_error'].iloc[mid_idx + 30], df['wt_nc'].iloc[mid_idx], 
                 'WT', fontsize=10, fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=line2.get_color(), alpha=0.7, edgecolor='none'))
    axes[0].text(df['current_error'].iloc[mid_idx + 35], df['sm_nc'].iloc[mid_idx], 
                 'SM', fontsize=10, fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=line3.get_color(), alpha=0.7, edgecolor='none'))
    
    axes[0].set_xlabel('Wartość błędu', fontsize=12)
    axes[0].set_ylabel('Ilość poprawnych (nc)', fontsize=12)
    axes[0].set_title('Ilość poprawnych a wartość błędu', fontsize=14)
    axes[0].legend(fontsize=10)
    axes[0].grid(True, alpha=0.3)
    
    #Bezpieczeństwo nic
    line4, = axes[1].plot(df['current_error'], df['maj_nic'], label='Większościowy', linewidth=4, markersize=8, alpha = 0.8)
    line5, = axes[1].plot(df['current_error'], df['wt_nic'], label='Wagowy', linewidth=2, markersize=6, alpha = 0.8)
    line6, = axes[1].plot(df['current_error'], df['sm_nic'], label='Wygładzający', linewidth=2, markersize=6, alpha = 0.8)
    
    axes[1].text(df['current_error'].iloc[mid_idx + 25], df['maj_nic'].iloc[mid_idx], 
                 'MAJ', fontsize=10, fontweight='bold', 
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=line4.get_color(), alpha=0.7, edgecolor='none'))
    axes[1].text(df['current_error'].iloc[mid_idx + 30], df['wt_nic'].iloc[mid_idx], 
                 'WT', fontsize=10, fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=line5.get_color(), alpha=0.7, edgecolor='none'))
    axes[1].text(df['current_error'].iloc[mid_idx + 35], df['sm_nic'].iloc[mid_idx], 
                 'SM', fontsize=10, fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=line6.get_color(), alpha=0.7, edgecolor='none'))
    
    axes[1].set_xlabel('Wartość błędu', fontsize=12)
    axes[1].set_ylabel('Ilość błędnych (nic)', fontsize=12)
    axes[1].set_title('Ilość błędnych a wartość błędu', fontsize=14)
    axes[1].legend(fontsize=10)
    axes[1].grid(True, alpha=0.3)

    # Detection (nd)
    line7, = axes[2].plot(df['current_error'], df['maj_nd'], label='Większościowy', linewidth=4, markersize=8, alpha = 0.8)
    line8, = axes[2].plot(df['current_error'], df['wt_nd'], label='Wagowy', linewidth=2, markersize=6, alpha = 0.8)
    line9, = axes[2].plot(df['current_error'], df['sm_nd'], label='Wygładzający', linewidth=2, markersize=6, alpha = 0.8)
    
    axes[2].text(df['current_error'].iloc[mid_idx + 25], df['maj_nd'].iloc[mid_idx], 
                 'MAJ', fontsize=10, fontweight='bold', 
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=line7.get_color(), alpha=0.7, edgecolor='none'))
    axes[2].text(df['current_error'].iloc[mid_idx + 30], df['wt_nd'].iloc[mid_idx], 
                 'WT', fontsize=10, fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=line8.get_color(), alpha=0.7, edgecolor='none'))
    axes[2].text(df['current_error'].iloc[mid_idx + 35], df['sm_nd'].iloc[mid_idx], 
                 'SM', fontsize=10, fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=line9.get_color(), alpha=0.7, edgecolor='none'))
    
    axes[2].set_xlabel('Wartość błędu', fontsize=12)
    axes[2].set_ylabel('Ilość odrzuconych (nd)', fontsize=12)
    axes[2].set_title('Ilość odrzuconych a wartość błędu', fontsize=14)
    axes[2].legend(fontsize=10)
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()