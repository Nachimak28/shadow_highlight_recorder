import os

os.environ.setdefault(
    'CSV_PATH', 'C:\\Users\HP\Desktop\OSS\shadow_highlight_recorder\data\Processing_needed_low_contrast_all_perfect_concensus_images_v2_with_means_medians.csv')

compulsory_column_names = ['status', 
                        'shadow_amount_percent', 
                        'shadow_tone_percent', 
                        'shadow_radius',
                        'highlight_amount_percent', 
                        'highlight_tone_percent',
                        'highlight_radius', 
                        'color_percent']