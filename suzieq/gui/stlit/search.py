from collections import deque
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
class SearchSessionState:
    '''Session state for Search page'''
    page: str = SuzieqMainPages.SEARCH.value
    search_text: str = ''
    past_df = None
    table: str = ''
    namespace: str = ''
    query_str: str = ''
    unique_query: dict = field(default_factory=dict)
    prev_results = deque(maxlen=5)


class SearchPage(SqGuiPage):
    '''Page for Path trace page'''
    _title: str = SuzieqMainPages.SEARCH.value
    _state = SearchSessionState()

    @property
    def add_to_menu(self):
        return True

    def build(self):
        self._get_state_from_url()
        self._create_sidebar()
        self._create_layout()
        self._render()

    def _get_state_from_url(self):
        pass

    def _create_layout(self) -> None:
        pass

    def _create_sidebar(self) -> None:
        pass

    def _sync_state(self) -> None:
        pass

    def _save_page_url(self) -> None:
        pass
