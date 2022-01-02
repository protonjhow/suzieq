import sys
import argparse
from collections import defaultdict
import base64

import streamlit as st

from suzieq.gui.stlit.guiutils import (get_image_dir, display_help_icon,
                                       get_main_session_by_id, SuzieqMainPages)
from suzieq.gui.stlit.pagecls import SqGuiPage
from suzieq.version import SUZIEQ_VERSION
from suzieq.shared.utils import sq_get_config_file


def set_horizontal_radio():
    '''Make the radio buttons horizontal'''
    st.write('<style>div.row-widget.stRadio > '
             'div{flex-direction:row;}</style>',
             unsafe_allow_html=True)


def set_vertical_radio():
    '''Make the radio buttons horizontal'''
    st.write('<style>div.row-widget.stRadio > '
             'div{flex-direction:column;}</style>',
             unsafe_allow_html=True)


def hide_st_index():
    '''CSS to hide table index rendered via st.table'''
    st.markdown("""
        <style>
        .table td:nth-child(1) {
            display: none;
        }
        .table th:nth-child(1) {
            display: none;
        }
        </style>
        """, unsafe_allow_html=True)


def display_title(page: str):
    '''Render the logo and the app name'''

    state = st.session_state
    menulist = state.menulist
    search_text = state.search_text

    LOGO_IMAGE = f'{get_image_dir()}/logo-small.jpg'
    st.markdown(
        """
        <style>
        .container {
            display: flex;
        }
        .logo-text {
            font-weight:700 !important;
            font-size:24px !important;
            color: purple !important;
            padding-top: 40px !important;
        }
        .logo-img {
            width: 20%;
            height: auto;
            float:right;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    title_col, _, page_col, srch_col = st.columns([2, 1, 2, 2])

    with open(LOGO_IMAGE, "rb") as f:
        img = base64.b64encode(f.read()).decode()

    with title_col:
        st.markdown(
            f"""
            <div class="container">
                <img class="logo-img" src="data:image/png;base64,
                {img}">
                <h1 style='color:purple;'>Suzieq</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

    sel_menulist = list(filter(lambda x: not x.startswith('_'), menulist))

    with srch_col:
        st.text(' ')
        search_str = st.text_input("Search", value=state.search_text,
                                   key='search', on_change=main_sync_state)
    if search_text is not None and (search_str != search_text):
        # We're assuming here that the page is titled Search
        page = 'Search'

    with page_col:
        # The empty writes are for aligning the pages link with the logo
        st.text(' ')
        srch_holder = st.empty()
        if page in sel_menulist:
            pageidx = sel_menulist.index(page)
        else:
            pageidx = sel_menulist.index('Status')
        set_horizontal_radio()
        if 'sq_page' not in state:
            page = srch_holder.radio('Page', sel_menulist, index=pageidx,
                                     key='sq_page',
                                     on_change=main_sync_state)
        else:
            page = srch_holder.radio('Page', sel_menulist, key='sq_page',
                                     on_change=main_sync_state)
            page = state.sq_page
        set_vertical_radio()
    return page, search_str


def main_sync_state():
    '''Sync search & page state on main Suzieq GUI page'''
    wsstate = st.session_state

    if wsstate.search_text != wsstate.search:
        wsstate.search_text = wsstate.search
        wsstate.page = wsstate.sq_page = 'Search'

    if wsstate.page != wsstate.sq_page:
        wsstate.page = wsstate.sq_page
        st.experimental_set_query_params(**{})
        if wsstate.page != 'Search':
            wsstate.search_text = ''


def build_pages(state):
    '''Build dict of page name and corresponding module'''

    pages = SqGuiPage.get_plugins()
    page_tbl = defaultdict(dict)

    for obj in pages.values():
        page = obj()
        if page.add_to_menu:
            page_tbl[page.title] = page.build

    return page_tbl


def apprun(*args):
    '''The main application routine'''

    if not args:
        args = sys.argv

    parser = argparse.ArgumentParser(args)
    parser.add_argument(
        "-c",
        "--config",
        type=str, help="alternate config file",
        default=None
    )
    userargs = parser.parse_args()
    config_file = sq_get_config_file(userargs.config)

    state = st.session_state
    state.config_file = config_file

    st.set_page_config(layout="wide",
                       page_title="Suzieq",
                       menu_items={
                           'About': f'Suzieq Version: {SUZIEQ_VERSION}'
                       })

    for key, val in [('pages', None),
                     ('menulist', []),
                     ('page', None),
                     ('search_text', ''),
                     ('sqobjs', {})]:
        if key not in state:
            state[key] = val

    if not state.menulist:
        state.pages = build_pages(state)
        # Hardcoding the order of these pages
        state.menulist = [SuzieqMainPages.STATUS.value,
                          SuzieqMainPages.XPLORE.value,
                          SuzieqMainPages.PATH.value,
                          SuzieqMainPages.SEARCH.value]
        for pg in state.pages:
            if pg not in state.menulist:
                state.menulist.append(pg)

    url_params = st.experimental_get_query_params()
    if url_params.get('page', ''):
        page = url_params['page']
        if isinstance(page, list):
            page = page[0]
        old_session_state = get_main_session_by_id(
            url_params.get('session', [''])[0])
        if old_session_state:
            if page == "_Path_Debug_":
                state.pages[page](old_session_state)
                st.stop()
            elif page == "_Help_":
                state.pages[page](old_session_state)
                st.stop()

        if isinstance(page, list):
            page = page[0]
    else:
        page = None

    if page is None:
        if state.page:
            page = state.page
        else:
            page = state.menulist[0]

    state.page = page

    page, search_text = display_title(page)

    if search_text != state.search_text:
        state.search_text = search_text
        state.page = page = 'Search'

    state.pages[page]()


if __name__ == '__main__':
    apprun()
