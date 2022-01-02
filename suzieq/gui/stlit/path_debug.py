from dataclasses import dataclass, field, asdict
from typing import List

import numpy as np
import pandas as pd
import streamlit as st

from suzieq.gui.stlit.guiutils import (sq_gui_style, gui_get_df,
                                       SuzieqMainPages)
from suzieq.gui.stlit.pagecls import SqGuiPage
from suzieq.sqobjects import get_sqobject, get_tables


@dataclass
class PageSessionState:
    '''Session state for status page'''
    page: str = 'Path Debug'


class PathDebugPage(SqGuiPage):
    '''Page for Path trace page'''
    _title = 'Path Debug'
    _failed_dfs_list = []

    @property
    def add_to_menu(self) -> bool:
        return False

    def build(self):
        pass

    def _get_state_from_url(self):
        pass

    def _create_sidebar(self) -> None:
        pass

    def _create_layout(self) -> None:
        pass

    def _render(self, layout: dict) -> None:
        pass

    def _sync_state(self) -> None:
        pass

    def _save_page_url(self) -> None:
        pass
