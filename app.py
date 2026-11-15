# Team Jwala - Flame in Freefall (NASA Space Apps 2026)
# SI disclosure: this file was written with help from Claude (Anthropic)
# and reviewed and edited by the team member.
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Flame in Freefall - Investigation Explorer", layout="wide")

@st.cache_data
def load():
    return pd.read_csv("data/investigations.csv")

df = load()

st.title("Flame in Freefall: Combustion Investigation Explorer")
st.caption("Team Jwala - NASA Space Apps Challenge 2026 - Kochi")
st.write(
    "A simple explorer for NASA microgravity combustion investigations "
    "catalogued in NASA's Physical Sciences Informatics (PSI). "
    "It shows what each investigation set out to do, not its measurements."
)

with st.sidebar:
    st.header("Filters")
    types = st.multiselect("Investigation type", sorted(df["type"].unique()),
                           default=sorted(df["type"].unique()))
    text = st.text_input("Search title or text")

view = df[df["type"].isin(types)]
if text:
    mask = view.apply(lambda r: text.lower() in " ".join(map(str, r.values)).lower(), axis=1)
    view = view[mask]

if view.empty:
    st.warning("No investigations match these filters.")
    st.stop()

c1, c2 = st.columns([2, 1])
with c1:
    st.subheader(f"Investigations ({len(view)})")
    st.dataframe(view[["investigation_id", "title", "type", "research_area"]],
                 use_container_width=True, hide_index=True)
with c2:
    counts = view["type"].value_counts().reset_index()
    counts.columns = ["type", "count"]
    st.plotly_chart(px.bar(counts, x="type", y="count", title="Investigations by type"),
                    use_container_width=True)

st.subheader("Details")
choice = st.selectbox("Choose an investigation", view["investigation_id"])
row = view[view["investigation_id"] == choice].iloc[0]
st.markdown(f"**{row['title']}** ({row['investigation_id']})")
st.markdown(f"**Objective (excerpt):** {row['objective_excerpt']}")
st.markdown(f"**Approach (excerpt):** {row['approach_excerpt']}")
st.caption(f"Source: {row['source']}")
extra = {"Flight platform": row.get("flight_platform"), "DOI": row.get("doi"), "License": row.get("license")}
for k, v in extra.items():
    if isinstance(v, str) and v:
        st.markdown(f"**{k}:** {v}")

try:
    samples = pd.read_csv("data/samples.csv")
    samples = samples[samples["investigation_id"] == choice]
except FileNotFoundError:
    samples = pd.DataFrame()
if not samples.empty:
    st.markdown("**Sample table (values as displayed on the PSI page)**")
    st.dataframe(samples.drop(columns=["investigation_id"]), hide_index=True,
                 use_container_width=True)
    st.caption("Only the rows visible on the PSI page when this was prepared are included "
               "(PSI-99 has 16 rows; 5 are shown here). Values are exactly as displayed and have "
               "not been re-interpreted; some PSI entries look like typos (e.g. '037 mm').")

st.divider()
st.caption(
    "Data: NASA Physical Sciences Informatics (PSI), psi.nasa.gov. Text excerpts are "
    "copied from PSI pages. This is a research-exploration prototype, not a validated "
    "or certified fire-safety tool. Built with AI assistance (Claude, Anthropic): "
    "code was SI-assisted; no model runs inside this app."
)
