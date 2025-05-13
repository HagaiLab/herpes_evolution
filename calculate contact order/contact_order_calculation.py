# contact order function with df for example

csu_data = pd.read_csv("csu_df_for_example.csv", index_col=0)

def calc_contact_order(csu_df, min_seq_distance = 4, prefix=""):
    df = csu_df[csu_df["residual_dist"] >= min_seq_distance]

    amino_dist_precentile = (df.groupby(["target_protein"])
        .agg(sum_residual_dist=("residual_dist","sum"),
             count_residual_dist=("residual_dist","count"))
        .reset_index()
        )
    amino_dist_precentile.columns = ["target_protein", "sum_residual_dist", "count_residual_dist"]
    amino_dist_precentile[prefix + "abs_mean_contact_order"] = amino_dist_precentile["sum_residual_dist"] / amino_dist_precentile["count_residual_dist"]
    amino_dist_precentile.drop(["sum_residual_dist", "count_residual_dist"], axis=1)

    return amino_dist_precentile

display(calc_contact_order(protein_data_csu))


