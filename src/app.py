import os
from PIL import Image
import streamlit as st
import numpy as np
import pandas as pd
from enums import Status
from config import compulsory_column_names
from utils import get_current_time, filter_images_by_status, shadow_highlight_correction
from layout import main_layout


st.write('Shadow highlight recorder')

df = pd.read_csv('..\data\low_contrast_all_perfect_concensus_images_v2_with_means_medians.csv')
df['processing_flag'] = np.logical_and(df.low_contrast_flag_upper_pencentile_50, df.low_contrast_flag_upper_pencentile_60_lower_percentile_30)

image_path_list = list(df[df.processing_flag == True].image_paths)

@st.cache
def read_csv_and_filter(csv_path):
    render_flag = False
    df = pd.read_csv(csv_path)
    df_column_names = list(df.columns)
    if set(compulsory_column_names).issubset(set(df_column_names)) == False:
        # st.write('Column name issue')s
        render_flag = False
    else:
        render_flag = True

    return render_flag, df


def show():

    csv_file_path = os.environ['CSV_PATH']
    render_flag, df = read_csv_and_filter(
        csv_path=csv_file_path)
    
    if render_flag:
        if "df" not in st.session_state:
            st.session_state.df = df.copy()
            # data_dict = df.T.to_dict()
            pending_df = st.session_state.df[st.session_state.df.status ==
                                             Status.pending.value]
            pending_start_index = pending_df.index[0]

            st.session_state.final_index = len(df)
            st.session_state.current_index = pending_start_index

        def record_data(record_data_dict):
            for k, v in record_data_dict.items():
                st.session_state.df.at[st.session_state.current_index,
                                   k] = v
            st.session_state.df.at[st.session_state.current_index,
                                   'status'] = 'done'
            # if st.session_state.current_index:
            if st.session_state.current_index < st.session_state.final_index:
                st.session_state.current_index += 1
        
        if st.session_state.current_index < st.session_state.final_index:
            image_path = st.session_state.df.loc[st.session_state.current_index, 'image_paths']

            image = np.array(Image.open(image_path))

            st.write(
                "Annotated:",
                st.session_state.current_index,
                "– Total:",
                st.session_state.final_index,
            )

            if st.session_state.current_index < st.session_state.final_index:
                shadow_amount, shadow_tone, highlight_amount, highlight_tone = main_layout(image=image)

                record_dict = {
                    'shadow_amount_percent': shadow_amount, 
                    'shadow_tone_percent': shadow_tone, 
                    'shadow_radius': 100,
                    'highlight_amount_percent': highlight_amount, 
                    'highlight_tone_percent': highlight_tone,
                    'highlight_radius': 100, 
                    'color_percent': 1
                }

                st.button('Next', on_click=record_data,
                                args=(record_dict,))

            else:
                st.success(
                    f"🎈 Done! All {st.session_state.final_index} images fixed."
                )
                st.session_state.df.to_csv(csv_file_path)

        st.button('Save intermediate data',
                  on_click=st.session_state.df.to_csv(csv_file_path))
    else:
        st.write('Not rendering, column issue')


if __name__ == "__main__":
    show()
            
