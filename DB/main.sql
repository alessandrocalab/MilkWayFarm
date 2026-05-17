SET SQLBLANKLINES ON --senza interpreta male le righe vuote

--Eliminazione schema precedente

@drop_all.sql


--Sezione: 1_prodotto

@DDL/1_prodotto/1_tipo_prodotto.sql
@DDL/1_prodotto/2_sostanza.sql
@DDL/1_prodotto/3_modalita_conservazione.sql

--Sezione: 2_struttura

@DDL/2_struttura/1_struttura.sql
@DDL/2_struttura/2_area_st.sql
@DDL/2_struttura/3_blocco_animale.sql
@DDL/2_struttura/4_scaffale.sql
@DDL/2_struttura/5_serbatoio.sql
@DDL/2_struttura/6_tipo_sensore.sql
@DDL/2_struttura/7_sensore.sql
@DDL/2_struttura/8_registrazione_sensore.sql
@DDL/2_struttura/9_cella_idroponica.sql

--Sezione: 3_animale

@DDL/3_animale/1_tipo_animale.sql
@DDL/3_animale/2_animale.sql
@DDL/3_animale/3_stadio_crescita.sql
@DDL/3_animale/4_nome_animale.sql
@DDL/3_animale/5_tipo_vaccino.sql
@DDL/3_animale/6_vaccinazione.sql
@DDL/3_animale/7_visita_veterinaria.sql
@DDL/3_animale/8_prescrizione_animale.sql
@DDL/3_animale/9_produzione_animale.sql

--Sezione: 4_agricoltura

@DDL/4_agricoltura/1_modalita_coltivazione.sql
@DDL/4_agricoltura/2_tipo_coltura.SQL
@DDL/4_agricoltura/3_ciclo_coltivazione.sql
@DDL/4_agricoltura/5_produzione_agricola.sql

--Sezione: 5_missione.sql

@DDL/5_missione.sql/1_missione_rifornimento.sql
@DDL/5_missione.sql/2_prodotto_missione.sql

--Sezione: 6_associazioni

@DDL/6_associazioni/1_stadio_crescita_prevede_dieta.sql
@DDL/6_associazioni/2_dieta_comprende_prodotto.sql
@DDL/6_associazioni/3_prodotto_contiene_sostanza.sql
@DDL/6_associazioni/4_stadio_crescita_intollerante_sostanza.sql
@DDL/6_associazioni/5_animale_allergico_sostanza.sql
@DDL/6_associazioni/6_animale_prevede_dieta_speciale.sql
@DDL/6_associazioni/7_prodotto_da_stadio_crescita.sql
@DDL/6_associazioni/8_prodotto_prevede_mod_cons.sql
@DDL/6_associazioni/9_animale_allocato_blocco.sql
@DDL/6_associazioni/10_cella_idr_rispetta_mod_colt.sql
@DDL/6_associazioni/11_tipo_colt_accetta_mod_colt.sql
@DDL/6_associazioni/12_tipo_coltura_tipo_prodotto.SQL
@DDL/6_associazioni/13_scaffale_rispetta_mod_cons.sql
@DDL/6_associazioni/14_serb_rispetta_mod_cons.sql
@DDL/6_associazioni/15_produzione_agricola_alloc_serb.sql
@DDL/6_associazioni/16_produzione_agricola_alloc_scaff.sql
@DDL/6_associazioni/17_produzione_animale_allocazione_serb.sql
@DDL/6_associazioni/18_produzione_animale_alloc_scaff.sql
@DDL/6_associazioni/19_prodotto_missione_alloc_serb.sql
@DDL/6_associazioni/20_prodotto_missione_alloc_scaff.sql
@DDL/6_associazioni/21_dealloc_prod_ciclo_colt_serb.sql
@DDL/6_associazioni/22_dealloc_prod_ciclo_colt_scaff.sql
@DDL/6_associazioni/23_dealloc_prod_blocco_animale_serb.sql
@DDL/6_associazioni/24_dealloc_prod_blocco_animale_scaff.sql


COMMIT;