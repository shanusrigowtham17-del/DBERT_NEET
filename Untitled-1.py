# -*- coding: utf-8 -*-
import csv

rows = []

def add(q, subject, chapter, difficulty, answer, a, b, c, d):
    rows.append({
        "questions": q,
        "subject": subject,
        "chapter": chapter,
        "difficulty": difficulty,
        "answer": answer,
        "option_a": a,
        "option_b": b,
        "option_c": c,
        "option_d": d,
        "year": 2015
    })

# ============ CHEMISTRY (1-45) ============

add("2,3-Dimethyl-2-butene can be prepared by heating which of the following compounds with a strong acid?",
    "Chemistry", "Hydrocarbons", "Medium", "d",
    "(CH3)2C=CH-CH2-CH3", "(CH3)2CH-CH2-CH=CH2",
    "(CH3)2CH-CH(CH3)-CH=CH2", "(CH3)3C-CH=CH2")

add("Gadolinium belongs to 4f series. Its atomic number is 64. Which of the following is the correct electronic configuration of gadolinium?",
    "Chemistry", "Periodic Table (d and f block elements)", "Medium", "a",
    "[Xe]4f7 5d1 6s2", "[Xe]4f6 5d2 6s2", "[Xe]4f8 6d2", "[Xe]4f9 5s1")

add("The formation of the oxide ion O2-(g) from oxygen atom requires first an exothermic and then an endothermic step. Thus the process of formation of O2- in gas phase is unfavourable though O2- is isoelectronic with neon. It is due to the fact that:",
    "Chemistry", "Classification of Elements and Periodicity", "Medium", "c",
    "Oxygen is more electronegative", "Addition of electron in oxygen results in larger size of the ion",
    "Electron repulsion outweighs the stability gained by achieving noble gas configuration",
    "O- ion has comparatively smaller size than oxygen atom")

add("The number of structural isomers possible from the molecular formula C3H9N is:",
    "Chemistry", "Amines", "Easy", "b", "2", "3", "4", "5")

add("If the equilibrium constant for N2(g) + O2(g) ⇌ 2NO(g) is K, the equilibrium constant for 1/2 N2(g) + 1/2 O2(g) ⇌ NO(g) will be:",
    "Chemistry", "Equilibrium", "Medium", "c", "K", "K^2", "K^(1/2)", "K/2")

add("Which one of the following pairs of solution is not an acidic buffer?",
    "Chemistry", "Equilibrium", "Medium", "c",
    "H2CO3 and Na2CO3", "H3PO4 and Na3PO4", "HClO4 and NaClO4", "CH3COOH and CH3COONa")

add("Aqueous solution of which of the following compounds is the best conductor of electric current?",
    "Chemistry", "Electrochemistry", "Easy", "d",
    "Ammonia, NH3", "Fructose, C6H12O6", "Acetic acid, C2H4O2", "Hydrochloric acid, HCl")

add("Caprolactam is used for the manufacture of:",
    "Chemistry", "Polymers", "Easy", "c", "Terylene", "Nylon-6,6", "Nylon-6", "Teflon")

add("On heating which of the following releases CO2 most easily?",
    "Chemistry", "s-Block Elements", "Medium", "a", "MgCO3", "CaCO3", "K2CO3", "Na2CO3")

add("Strong reducing behaviour of H3PO2 is due to:",
    "Chemistry", "p-Block Elements (Group 15)", "Medium", "c",
    "High oxidation state of phosphorus", "Presence of two -OH groups and one P-H bond",
    "Presence of one -OH group and two P-H bonds", "High electron gain enthalpy of phosphorus")

add("Decreasing order of stability of O2, O2-, O2+ and O2(2-) is:",
    "Chemistry", "Chemical Bonding and Molecular Structure", "Medium", "c",
    "O2 > O2+ > O2(2-) > O2-", "O2- > O2(2-) > O2+ > O2",
    "O2+ > O2 > O2- > O2(2-)", "O2(2-) > O2- > O2 > O2+")

add("The number of water molecules is maximum in:",
    "Chemistry", "Some Basic Concepts of Chemistry (Mole Concept)", "Easy", "b",
    "18 gram of water", "18 moles of water", "18 molecules of water", "1.8 gram of water")

add("In which of the following pairs, both the species are not isostructural?",
    "Chemistry", "Chemical Bonding and Molecular Structure", "Hard", "b",
    "NH3, PH3", "XeF4, XeO4", "SiCl4, PCl4+", "Diamond, silicon carbide")

add("In the reaction with HCl, an alkene reacts in accordance with the Markovnikov's rule, to give a product 1-chloro-1-methylcyclohexane. The possible reaction alkene is (methylenecyclohexane and 1-methylcyclohexene):",
    "Chemistry", "Hydrocarbons", "Medium", "c",
    "Methylenecyclohexane only", "1-Methylcyclohexene only",
    "Methylenecyclohexane and 1-methylcyclohexene", "3-Methylcyclohexene")

add("Assuming complete ionization, same moles of which of the following compounds will require the least amount of acidified KMnO4 for complete oxidation?",
    "Chemistry", "Redox Reactions", "Medium", "c",
    "FeC2O4", "Fe(NO2)2", "FeSO4", "FeSO3")

add("Reaction of phenol with chloroform in presence of dilute sodium hydroxide finally introduces which one of the following functional group? (Reimer-Tiemann reaction)",
    "Chemistry", "Alcohols, Phenols and Ethers", "Medium", "b",
    "-CHCl2", "-CHO", "-CH2Cl", "-COOH")

add("The vacant space in bcc lattice unit cell is:",
    "Chemistry", "Solid State", "Medium", "b", "23%", "32%", "26%", "48%")

add("Which of the statements given below is incorrect?",
    "Chemistry", "p-Block Elements (Group 16 and 17)", "Hard", "b",
    "ONF is isoelectronic with O2N-", "OF2 is an oxide of fluorine",
    "Cl2O7 is an anhydride of perchloric acid", "O3 molecule is bent")

add("The name of complex ion, [Fe(CN)6]3- is:",
    "Chemistry", "Coordination Compounds", "Medium", "b",
    "Tricyanoferrate (III) ion", "Hexacyanidoferrate (III) ion",
    "Hexacyanoiron (III) ion", "Hexacyanitoferrate (III) ion")

add("If Avogadro number NA is changed from 6.022x10^23 mol-1 to 6.022x10^20 mol-1, this would change:",
    "Chemistry", "Some Basic Concepts of Chemistry (Mole Concept)", "Medium", "d",
    "The ratio of chemical species to each other in a balanced equation",
    "The ratio of elements to each other in a compound",
    "The definition of mass in units of grams", "The mass of one mole of carbon")

add("Which of the following statements is not correct for a nucleophile?",
    "Chemistry", "Organic Chemistry - Basic Principles (GOC)", "Medium", "c",
    "Nucleophiles attack low electron density sites", "Nucleophiles are not electron seeking",
    "Nucleophile is a Lewis acid", "Ammonia is a nucleophile")

add("A gas such as carbon monoxide would be most likely to obey the ideal gas law at:",
    "Chemistry", "States of Matter", "Easy", "c",
    "High temperatures and high pressures", "Low temperatures and low pressures",
    "High temperatures and low pressures", "Low temperatures and high pressures")

add("The hybridization involved in complex [Ni(CN)4]2- is: (Atomic number of Ni = 28)",
    "Chemistry", "Coordination Compounds", "Medium", "c",
    "d2sp2", "d2sp3", "dsp2", "sp3")

add("The heat of combustion of carbon to CO2 is -393.5 kJ/mol. The heat released upon formation of 35.2 g of CO2 from carbon and oxygen gas is:",
    "Chemistry", "Thermodynamics", "Medium", "c",
    "-630 kJ", "-3.15 kJ", "-315 kJ", "+315 kJ")

add("20.0 g of a magnesium carbonate sample decomposes on heating to give carbon dioxide and 8.0 g magnesium oxide. What will be the percentage purity of magnesium carbonate in the sample? (Atomic weight: Mg = 24)",
    "Chemistry", "Stoichiometry (Mole Concept)", "Medium", "b", "60", "84", "75", "96")

add("What is the mole fraction of the solute in a 1.00 m aqueous solution?",
    "Chemistry", "Solutions", "Medium", "b", "0.0354", "0.0177", "0.177", "1.770")

add("The correct statement regarding defects in crystalline solids is:",
    "Chemistry", "Solid State", "Medium", "a",
    "Frenkel defect is a dislocation defect", "Frenkel defect is found in halides of alkaline metals",
    "Schottky defects have no effect on the density of crystalline solids",
    "Frenkel defects decrease the density of crystalline solids")

add("The stability of +1 oxidation state among Al, Ga, In and Tl increases in the sequence:",
    "Chemistry", "p-Block Elements (Group 13)", "Medium", "d",
    "Tl < In < Ga < Al", "In < Tl < Ga < Al", "Ga < In < Al < Tl", "Al < Ga < In < Tl")

add("Two possible stereo-structures of CH3CHOH.COOH, which are optically active, are called:",
    "Chemistry", "Stereochemistry / Organic Chemistry Basics", "Medium", "a",
    "Enantiomers", "Mesomers", "Diastereomers", "Atropisomers")

add("The reaction of aniline with benzoyl chloride in presence of NaOH to form N-phenylbenzamide is known by the name:",
    "Chemistry", "Amines", "Medium", "b",
    "Acetylation reaction", "Schotten-Baumann reaction", "Friedel-Craft's reaction", "Perkin's reaction")

add("The sum of coordination number and oxidation number of metal M in the complex [M(en)2(C2O4)]Cl (where en is ethylenediamine) is:",
    "Chemistry", "Coordination Compounds", "Medium", "c", "7", "8", "9", "6")

add("Reaction of a carbonyl compound with one of the following reagents involves nucleophilic addition followed by elimination of water. The reagent is:",
    "Chemistry", "Aldehydes, Ketones and Carboxylic Acids", "Medium", "d",
    "Hydrocyanic acid", "Sodium hydrogen sulphite", "A Grignard reagent",
    "Hydrazine in presence of feebly acidic solution")

add("Which one of the following esters gets hydrolyzed most easily under alkaline conditions?",
    "Chemistry", "Aldehydes, Ketones and Carboxylic Acids", "Medium", "c",
    "Phenyl acetate", "4-Chlorophenyl acetate", "4-Nitrophenyl acetate", "4-Methoxyphenyl acetate")

add("In an SN1 reaction on chiral centres, there is:",
    "Chemistry", "Haloalkanes and Haloarenes", "Medium", "d",
    "100% retention", "100% inversion", "100% racemization",
    "Inversion more than retention leading to partial racemization")

add("The rate constant of the reaction A -> B is 0.6x10^-3 mole per second. If the concentration of A is 5M, then concentration of B after 20 minutes is:",
    "Chemistry", "Chemical Kinetics", "Medium", "b", "0.36 M", "0.72 M", "1.08 M", "3.60 M")

add("What is the pH of the resulting solution when equal volumes of 0.1 M NaOH and 0.01 M HCl are mixed?",
    "Chemistry", "Equilibrium (Ionic Equilibrium)", "Medium", "c", "7.0", "1.04", "12.65", "2.0")

add("Number of possible isomers for the complex [Co(en)2Cl2]Cl will be (en = ethylene diamine):",
    "Chemistry", "Coordination Compounds", "Hard", "a", "3", "4", "2", "1")

add("The variation of the boiling points of the hydrogen halides is in the order HF > HI > HBr > HCl. What explains the higher boiling point of hydrogen fluoride?",
    "Chemistry", "p-Block Elements (Group 17) / Hydrogen Bonding", "Easy", "d",
    "The bond energy of HF molecules is greater than in other hydrogen halides",
    "The effect of nuclear shielding is much reduced in fluorine which polarizes the HF molecule",
    "The electronegativity of fluorine is much higher than for other elements in the group",
    "There is strong hydrogen bonding between HF molecules")

add("What is the mass of the precipitate formed when 50 mL of 16.9% solution of AgNO3 is mixed with 50 mL of 5.8% NaCl solution?",
    "Chemistry", "Stoichiometry (Mole Concept)", "Medium", "a", "7 g", "14 g", "28 g", "3.5 g")

add("The oxidation of benzene by V2O5 in the presence of air produces:",
    "Chemistry", "Hydrocarbons", "Medium", "d",
    "Benzoic acid", "Benzaldehyde", "Benzoic anhydride", "Maleic anhydride")

add("Which of the following is not the product of dehydration of 1-tert-butyl... (1-methylcyclohexanol with tert-butyl substituent) alcohol?",
    "Chemistry", "Alcohols, Phenols and Ethers", "Hard", "d",
    "1-(prop-1-en-1-yl)cyclohexene isomer 1", "1-(prop-1-en-1-yl)cyclohexene isomer 2",
    "1-(prop-2-en-1-yl)cyclohexene", "1-(but-2-yl)cyclohexene")

add("Method by which Aniline cannot be prepared is:",
    "Chemistry", "Amines", "Medium", "b",
    "Reduction of nitrobenzene with H2/Pd in ethanol",
    "Potassium salt of phthalimide treated with chlorobenzene followed by hydrolysis with aqueous NaOH solution",
    "Hydrolysis of phenylisocyanide with acidic solution",
    "Degradation of benzamide with bromine in alkaline solution")

add("Which of the following reaction(s) can be used for the preparation of alkyl halides? (i) CH3CH2OH+HCl/anhyd.ZnCl2 (ii) CH3CH2OH+HCl (iii) (CH3)3COH+HCl (iv) (CH3)2CHOH+HCl/anhyd.ZnCl2",
    "Chemistry", "Haloalkanes and Haloarenes", "Medium", "c",
    "IV only", "III and IV only", "I, III and IV only", "I and II only")

add("Which is the correct order of increasing energy of the listed orbitals in the atom of titanium? (At. No. Z=22)",
    "Chemistry", "Structure of Atom", "Easy", "b",
    "3s 3p 3d 4s", "3s 3p 4s 3d", "3s 4s 3p 3d", "4s 3s 3p 3d")

add("In the extraction of copper from its sulphide ore, the metal is finally obtained by the reduction of cuprous oxide with:",
    "Chemistry", "General Principles and Processes of Isolation of Elements (Metallurgy)", "Medium", "b",
    "Copper (I) sulphide", "Sulphur dioxide", "Iron (II) sulphide", "Carbon monoxide")

# ============ BIOLOGY (46-135) ============

add("Root pressure is usually acidic because:",
    "Biology", "Transport in Plants", "Medium", "b",
    "Increase in transpiration", "Active absorption", "Low osmotic potential in soil", "Passive absorption")

add("Which one is a wrong statement?",
    "Biology", "Plant Kingdom", "Medium", "c",
    "Brown algae have chlorophyll a and c, and fucoxanthin",
    "Archegonia are found in Bryophyta, Pteridophyta and Gymnosperms",
    "Mucor has biflagellate zoospores", "Haploid endosperm is typical feature of Gymnosperms")

add("Which of the following structures is not found in prokaryotic cells?",
    "Biology", "Cell: The Unit of Life", "Easy", "b",
    "Plasma membrane", "Nuclear envelope", "Ribosome", "Mesosome")

add("Which one of the following animals has two separate circulatory pathways?",
    "Biology", "Body Fluids and Circulation", "Medium", "d",
    "Shark", "Frog", "Lizard", "Whale")

add("Most animals that live in deep oceanic waters are:",
    "Biology", "Ecosystem", "Medium", "c",
    "Detritivores", "Primary consumers", "Secondary consumers", "Tertiary consumers")

add("An association of individuals of different species living in the same habitat and having functional interactions is:",
    "Biology", "Organisms and Populations", "Easy", "c",
    "Population", "Ecological niche", "Biotic community", "Ecosystem")

add("The oxygen evolved during photosynthesis comes from water molecules. Which one of the following pairs of elements is involved in this reaction?",
    "Biology", "Photosynthesis in Higher Plants", "Medium", "b",
    "Magnesium and Chlorine", "Manganese and Chlorine", "Manganese and Potassium", "Magnesium and Molybdenum")

add("Axile placentation is present in:",
    "Biology", "Morphology of Flowering Plants", "Medium", "c",
    "Argemone", "Dianthus", "Lemon", "Pea")

add("In which of the following both pairs have correct combination (gaseous vs sedimentary nutrient cycle)?",
    "Biology", "Ecosystem", "Medium", "b",
    "Gaseous: Sulphur and Phosphorus; Sedimentary: Carbon and Nitrogen",
    "Gaseous: Carbon and Nitrogen; Sedimentary: Sulphur and Phosphorus",
    "Gaseous: Carbon and sulphur; Sedimentary: Nitrogen and phosphorus",
    "Gaseous: Nitrogen and sulphur; Sedimentary: Carbon and Phosphorus")

add("In mammalian eye, the 'fovea' is the center of the visual field, where:",
    "Biology", "Neural Control and Coordination", "Medium", "b",
    "More rods than cones are found", "High density of cones occur, but has no rods",
    "The optic nerve leaves the eye", "Only rods are present")

add("Choose the wrong statement:",
    "Biology", "Plant Kingdom / Microbes", "Medium", "d",
    "Yeast is unicellular and useful in fermentation", "Penicillium is multicellular and produces antibiotics",
    "Neurospora is used in the study of biochemical genetics", "Morels and truffles are poisonous mushrooms")

add("Which of the following are not membrane-bound?",
    "Biology", "Cell: The Unit of Life", "Easy", "c",
    "Mesosomes", "Vacuoles", "Ribosomes", "Lysosomes")

add("In which of the following interactions both partners are adversely affected?",
    "Biology", "Organisms and Populations", "Easy", "b",
    "Mutualism", "Competition", "Predation", "Parasitism")

add("A colour blind man marries a woman with normal sight who has no history of colour blindness in her family. What is the probability of their grandson being colour blind?",
    "Biology", "Principles of Inheritance and Variation", "Medium", "b", "0.25", "0.5", "1", "Nil")

add("Ectopic pregnancies are referred to as:",
    "Biology", "Human Reproduction", "Easy", "c",
    "Pregnancies terminated due to hormonal imbalance", "Pregnancies with genetic abnormality",
    "Implantation of embryo at site other than uterus", "Implantation of defective embryo in the uterus")

add("Cellular organelles with membranes are:",
    "Biology", "Cell: The Unit of Life", "Easy", "a",
    "Lysosomes, Golgi apparatus and mitochondria", "Nuclei, ribosomes and mitochondria",
    "Chromosomes, ribosomes and endoplasmic reticulum", "Endoplasmic reticulum, ribosomes and nuclei")

add("Cell wall is absent in:",
    "Biology", "Biological Classification", "Easy", "d",
    "Nostoc", "Aspergillus", "Funaria", "Mycoplasma")

add("The term 'linkage' was coined by:",
    "Biology", "Principles of Inheritance and Variation", "Easy", "b",
    "W. Sutton", "T.H. Morgan", "T. Boveri", "G. Mendel")

add("Which of the following biomolecules does have a phosphodiester bond?",
    "Biology", "Biomolecules", "Medium", "a",
    "Nucleic acids in a nucleotide", "Fatty acids in a diglyceride",
    "Monosaccharides in a polysaccharide", "Amino acids in a polypeptide")

add("The primary dentition in human differs from permanent dentition in not having one of the following type of teeth:",
    "Biology", "Digestion and Absorption", "Easy", "c", "Incisors", "Canine", "Premolars", "Molars")

add("A protoplast is a cell:",
    "Biology", "Cell: The Unit of Life", "Easy", "a",
    "Without division", "Without plasma membrane", "Without nucleus", "Undergoing division")

add("In which group of organisms the cell walls form two thin overlapping shells which fit together?",
    "Biology", "Biological Classification", "Medium", "b",
    "Slime moulds", "Chrysophytes", "Euglenoids", "Dinoflagellates")

add("The DNA molecule to which the gene of interest is integrated for cloning is called:",
    "Biology", "Biotechnology: Principles and Processes", "Easy", "c",
    "Carrier", "Transformer", "Vector", "Template")

add("Male gametophyte in angiosperms produces:",
    "Biology", "Sexual Reproduction in Flowering Plants", "Medium", "b",
    "Three sperms", "Two sperms and a vegetative cell", "Single sperm and a vegetative cell",
    "Single sperm and two vegetative cells")

add("Coconut water from a tender coconut is:",
    "Biology", "Sexual Reproduction in Flowering Plants", "Medium", "c",
    "Degenerated nucellus", "Immature embryo", "Free nuclear endosperm", "Innermost layers of the seed coat")

add("The species confined to a particular region and not found elsewhere is termed as:",
    "Biology", "Biodiversity and Conservation", "Easy", "d",
    "Rare", "Keystone", "Alien", "Endemic")

add("Metagenesis refers to:",
    "Biology", "Animal Kingdom", "Medium", "c",
    "Presence of a segmented body and parthenogenetic mode of reproduction",
    "Presence of different morphic forms",
    "Alternation of generation between asexual and sexual phases of an organism",
    "Occurrence of a drastic change in form during post-embryonic development")

add("The enzyme that is not present in succus entericus is:",
    "Biology", "Digestion and Absorption", "Medium", "c",
    "Lipase", "Maltase", "Nucleases", "Nucleosidase")

add("Eutrophication of water bodies leading to killing of fishes is mainly due to non-availability of:",
    "Biology", "Environmental Issues", "Easy", "a", "Oxygen", "Food", "Light", "Essential minerals")

add("The function of the gap junction is to:",
    "Biology", "Structural Organisation in Animals", "Medium", "c",
    "Stop substance from leaking across a tissue",
    "Perform cementing to keep neighbouring cells together",
    "Facilitate communication between adjoining cells by connecting the cytoplasm for rapid transfer of ions, small molecules and some large molecules",
    "Separate two cells from each other")

add("Match the following list of microbes and their importance: (a) Saccharomyces cerevisiae (b) Monascus purpureus (c) Trichoderma polysporum (d) Propionibacterium shermanii with (i) Immunosuppressive agents (ii) Ripening of Swiss cheese (iii) Commercial production of ethanol (iv) Blood-cholesterol lowering agents",
    "Biology", "Microbes in Human Welfare", "Medium", "b",
    "(iii)(i)(iv)(ii)", "(iii)(iv)(i)(ii)", "(iv)(iii)(ii)(i)", "(iv)(ii)(i)(iii)")

add("Arrange the following events of meiosis in correct sequence: (a) Crossing over (b) Synapsis (c) Terminalisation of chiasmata (d) Disappearance of nucleolus",
    "Biology", "Cell Cycle and Cell Division", "Medium", "c",
    "(b),(c),(d),(a)", "(b),(a),(d),(c)", "(b),(a),(c),(d)", "(a),(b),(c),(d)")

add("The cutting of DNA at specific locations became possible with the discovery of:",
    "Biology", "Biotechnology: Principles and Processes", "Easy", "b",
    "Ligases", "Restriction enzymes", "Probes", "Selectable markers")

add("During biological nitrogen fixation, inactivation of nitrogenase by oxygen poisoning is prevented by:",
    "Biology", "Mineral Nutrition", "Medium", "b",
    "Cytochrome", "Leghaemoglobin", "Xanthophyll", "Carotene")

add("Grafted kidney may be rejected in a patient due to:",
    "Biology", "Human Health and Disease", "Medium", "c",
    "Innate immune response", "Humoral immune response", "Cell-mediated immune response", "Passive immune response")

add("The body cells in cockroach discharge their nitrogenous waste in the haemolymph mainly in the form of:",
    "Biology", "Excretory Products and their Elimination / Animal Kingdom", "Medium", "c",
    "Calcium carbonate", "Ammonia", "Potassium urate", "Urea")

add("Filiform apparatus is characteristic feature of:",
    "Biology", "Sexual Reproduction in Flowering Plants", "Medium", "a",
    "Synergids", "Generative cell", "Nucellar embryo", "Aleurone cell")

add("Acid rain is caused by increase in the atmospheric concentration of:",
    "Biology", "Environmental Issues", "Easy", "b",
    "O3 and dust", "SO2 and NO2", "SO3 and CO", "CO2 and CO")

add("The wheat grain has an embryo with one large, shield-shaped cotyledon known as:",
    "Biology", "Morphology of Flowering Plants", "Medium", "d",
    "Coleoptile", "Epiblast", "Coleorrhiza", "Scutellum")

add("Among china rose, mustard, brinjal, potato, guava, cucumber, onion and tulip, how many plants have superior ovary?",
    "Biology", "Morphology of Flowering Plants", "Medium", "c", "Four", "Five", "Six", "Three")

add("Which of the following is not a function of the skeletal system?",
    "Biology", "Locomotion and Movement", "Easy", "d",
    "Locomotion", "Production of erythrocytes", "Storage of minerals", "Production of body heat")

add("Golden rice is a genetically modified crop plant where the incorporated gene is meant for biosynthesis of:",
    "Biology", "Biotechnology and its Applications", "Easy", "a",
    "Vitamin A", "Vitamin B", "Vitamin C", "Omega 3")

add("Chromatophores take part in:",
    "Biology", "Biological Classification (Monera)", "Medium", "b",
    "Respiration", "Photosynthesis", "Growth", "Movement")

add("Select the wrong statement:",
    "Biology", "Biological Classification (Viruses)", "Medium", "b",
    "Mosaic disease in tobacco and AIDS in human being are caused by viruses",
    "The viroids were discovered by D.J. Ivanowski",
    "W.M. Stanley showed that viruses could be crystallized",
    "The term 'contagium vivum fluidum' was coined by M.W. Beijerinck")

add("A pleiotropic gene:",
    "Biology", "Principles of Inheritance and Variation", "Medium", "a",
    "Controls multiple traits in an individual", "Is expressed only in primitive plants",
    "Is a gene evolved during Pliocene", "Controls a trait only in combination with another gene")

add("Human urine is usually acidic because:",
    "Biology", "Excretory Products and their Elimination", "Medium", "a",
    "Hydrogen ions are actively secreted into the filtrate",
    "The sodium transporter exchanges one hydrogen ion for each sodium ion, in peritubular capillaries",
    "Excreted plasma proteins are acidic", "Potassium and sodium exchange generates acidity")

add("Auxin can be bioassayed by:",
    "Biology", "Plant Growth and Development", "Medium", "b",
    "Lettuce hypocotyl elongation", "Avena coleoptile curvature", "Hydroponics", "Potometer")

add("Which of the following events is not associated with ovulation in human female?",
    "Biology", "Human Reproduction", "Medium", "b",
    "LH surge", "Decrease in estradiol", "Full development of Graafian follicle", "Release of secondary oocyte")

add("Body having meshwork of cells, internal cavities lined with food filtering flagellated cells and indirect development are the characteristics of phylum:",
    "Biology", "Animal Kingdom", "Medium", "c",
    "Protozoa", "Coelenterata", "Porifera", "Mollusca")

add("Which one of the following hormones is not involved in sugar metabolism?",
    "Biology", "Chemical Coordination and Integration", "Medium", "c",
    "Glucagon", "Cortisone", "Aldosterone", "Insulin")

add("Which of the following diseases is caused by a protozoan?",
    "Biology", "Human Health and Disease", "Medium", "d",
    "Blastomycosis", "Syphilis", "Influenza", "Babesiosis")

add("Outbreeding is an important strategy of animal husbandry because it:",
    "Biology", "Strategies for Enhancement in Food Production", "Medium", "d",
    "Exposes harmful recessive genes that are eliminated by selection",
    "Helps in accumulation of superior genes", "Is useful in producing purelines of animals",
    "Is useful in overcoming inbreeding depression")

add("A childless couple can be assisted to have a child through a technique called GIFT. The full form of this technique is:",
    "Biology", "Reproductive Health", "Easy", "c",
    "Germ cell internal fallopian transfer", "Gamete inseminated fallopian transfer",
    "Gamete intra fallopian transfer", "Gamete internal fertilization and transfer")

add("A jawless fish, which lays eggs in fresh water and whose ammocoetes larvae after metamorphosis return to the ocean is:",
    "Biology", "Animal Kingdom", "Hard", "a",
    "Petromyzon", "Eptatretus", "Myxine", "Neomyxine")

add("The structures that help some bacteria to attach to rocks and/or host tissues are:",
    "Biology", "Biological Classification (Monera)", "Medium", "c",
    "Holdfast", "Rhizoids", "Fimbriae", "Mesosomes")

add("If you suspect major deficiency of antibodies in a person, to which of the following would you look for confirmatory evidence?",
    "Biology", "Human Health and Disease", "Medium", "a",
    "Serum globulins", "Fibrinogen in plasma", "Serum albumins", "Haemocytes")

add("In human females, meiosis-II is not completed until?",
    "Biology", "Human Reproduction", "Medium", "c", "Birth", "Puberty", "Fertilization", "Uterine implantation")

add("Which of the following layers in an antral follicle is acellular?",
    "Biology", "Human Reproduction", "Medium", "a",
    "Zona pellucida", "Granulosa", "Theca interna", "Stroma")

add("In his classic experiments on pea plants, Mendel did not use:",
    "Biology", "Principles of Inheritance and Variation", "Easy", "c",
    "Flower position", "Seed colour", "Pod length", "Seed shape")

add("Which one of the following fruits is parthenocarpic?",
    "Biology", "Sexual Reproduction in Flowering Plants", "Easy", "a",
    "Banana", "Brinjal", "Apple", "Jackfruit")

add("In angiosperms, microsporogenesis and megasporogenesis:",
    "Biology", "Sexual Reproduction in Flowering Plants", "Easy", "d",
    "Occur in ovule", "Occur in anther", "Form gametes without further divisions", "Involve meiosis")

add("A gene showing codominance has:",
    "Biology", "Principles of Inheritance and Variation", "Medium", "a",
    "Both alleles independently expressed in the heterozygote", "One allele dominant on the other",
    "Alleles tightly linked on the same chromosome", "Alleles that are recessive to each other")

add("The chitinous exoskeleton of arthropods is formed by the polymerisation of:",
    "Biology", "Animal Kingdom / Biomolecules", "Medium", "d",
    "Lipoglycans", "Keratin sulphate and chondroitin sulphate", "D-glucosamine", "N-acetyl glucosamine")

add("The imperfect fungi which are decomposers of litter and help in mineral cycling belong to:",
    "Biology", "Plant Kingdom", "Medium", "b",
    "Ascomycetes", "Deuteromycetes", "Basidiomycetes", "Phycomycetes")

add("The wings of a bird and the wings of an insect are:",
    "Biology", "Evolution", "Medium", "c",
    "Homologous structures and represent convergent evolution",
    "Homologous structures and represent divergent evolution",
    "Analogous structures and represent convergent evolution",
    "Phylogenetic structures and represent divergent evolution")

add("Flowers are unisexual in:",
    "Biology", "Morphology of Flowering Plants", "Easy", "c",
    "Onion", "Pea", "Cucumber", "China rose")

add("Increase in concentration of the toxicant at successive trophic levels is known as:",
    "Biology", "Environmental Issues", "Easy", "b",
    "Biogeochemical cycling", "Biomagnification", "Biodeterioration", "Biotransformation")

add("Destruction of the anterior horn cells of the spinal cord would result in loss of:",
    "Biology", "Neural Control and Coordination", "Medium", "c",
    "Integrating impulses", "Sensory impulses", "Voluntary motor impulses", "Commissural impulses")

add("Roots play insignificant role in absorption of water in:",
    "Biology", "Transport in Plants", "Medium", "c",
    "Wheat", "Sunflower", "Pistia", "Pea")

add("Match the columns and identify the correct option: (a) Thylakoids (b) Cristae (c) Cisternae (d) Chromatin with (i) Disc-shaped sacs in Golgi apparatus (ii) Condensed structure of DNA (iii) Flat membranous sacs in stroma (iv) Infoldings in mitochondria",
    "Biology", "Cell: The Unit of Life", "Medium", "c",
    "(iii)(iv)(ii)(i)", "(iv)(iii)(i)(ii)", "(iii)(iv)(i)(ii)", "(iii)(i)(iv)(ii)")

add("Identify the correct order of organisation of genetic material from largest to smallest:",
    "Biology", "Molecular Basis of Inheritance", "Medium", "d",
    "Chromosome, genome, nucleotide, gene", "Chromosome, gene, genome, nucleotide",
    "Genome, chromosomes, nucleotide, gene", "Genome, chromosome, gene, nucleotide")

add("Which one of the following hormones though synthesized elsewhere, is stored and released by the master gland?",
    "Biology", "Chemical Coordination and Integration", "Medium", "b",
    "Melanocyte stimulating hormone", "Antidiuretic hormone", "Luteinizing hormone", "Prolactin")

add("Read the different components (a) Secondary cortex (b) Wood (c) Secondary phloem (d) Phellem and tell the correct order of arrangement from outer side to inner side in a woody dicot stem:",
    "Biology", "Anatomy of Flowering Plants", "Medium", "d",
    "(d),(c),(a),(b)", "(c),(d),(b),(a)", "(a),(b),(d),(c)", "(d),(a),(c),(b)")

add("Which of the following joints would allow no movement?",
    "Biology", "Locomotion and Movement", "Easy", "b",
    "Ball and Socket joint", "Fibrous joint", "Cartilaginous joint", "Synovial joint")

add("Which one of the following is not applicable to RNA?",
    "Biology", "Molecular Basis of Inheritance", "Medium", "a",
    "Chargaff's rule", "Complementary base pairing", "5' phosphoryl and 3' hydroxyl ends",
    "Heterocyclic nitrogenous bases")

add("Doctors use stethoscope to hear the sound produced during each cardiac cycle. The second sound is heard when:",
    "Biology", "Body Fluids and Circulation", "Medium", "d",
    "AV node receives signal from SA node", "AV valves open up",
    "Ventricular walls vibrate due to gushing of blood from atria",
    "Semilunar valves close down after the blood flows into vessels from ventricles")

add("During ecological succession:",
    "Biology", "Ecosystem", "Medium", "b",
    "The changes lead to a community that is in near equilibrium with the environment and is called pioneer community",
    "The gradual and predictable change in species composition occurs in a given area",
    "The establishment of a new biotic community is very fast in its primary phase",
    "The number and types of animals remain constant")

add("In the given human pedigree, the filled symbols represent the affected individuals. Identify the type of given pedigree.",
    "Biology", "Principles of Inheritance and Variation", "Hard", "d",
    "X-linked dominant", "Autosomal dominant", "X-linked recessive", "Autosomal recessive")

add("Balbiani rings are sites of:",
    "Biology", "Molecular Basis of Inheritance", "Medium", "a",
    "RNA and protein synthesis", "Lipid synthesis", "Nucleotide synthesis", "Polysaccharide synthesis")

add("Name the pulmonary disease in which alveolar surface area involved in gas exchange is drastically reduced due to damage in the alveolar walls:",
    "Biology", "Breathing and Exchange of Gases", "Easy", "c",
    "Asthma", "Pleurisy", "Emphysema", "Pneumonia")

add("Which of the following is the most suitable indicator of SO2 pollution in the environment?",
    "Biology", "Environmental Issues", "Easy", "b",
    "Fungi", "Lichens", "Conifers", "Algae")

add("Satellite DNA is important because it:",
    "Biology", "Molecular Basis of Inheritance", "Medium", "c",
    "Codes for enzymes needed for DNA replication", "Codes for proteins needed in cell cycle",
    "Shows high degree of polymorphism in population and also the same degree of polymorphism in an individual, which is heritable from parents to children",
    "Does not code for proteins and is same in all members of the population")

add("Industrial melanism is an example of:",
    "Biology", "Evolution", "Medium", "c",
    "Neo Lamarckism", "Neo Darwinism", "Natural selection", "Mutation")

add("A column of water within xylem vessels of tall trees does not break under its weight because of:",
    "Biology", "Transport in Plants", "Medium", "c",
    "Positive root pressure", "Dissolved sugars in water", "Tensile strength of water",
    "Lignification of xylem vessels")

add("The introduction of t-DNA into plants involves:",
    "Biology", "Biotechnology: Principles and Processes", "Easy", "b",
    "Allowing the plant roots to stand in water", "Infection of the plant by Agrobacterium tumefaciens",
    "Altering the pH of the soil, then heat shocking the plants", "Exposing the plants to cold for a brief period")

add("Pick up the wrong statement:",
    "Biology", "Biological Classification", "Medium", "a",
    "Nuclear membrane is present in Monera", "Cell wall is absent in Animalia",
    "Protista have photosynthetic and heterotrophic modes of nutrition", "Some fungi are edible")

add("In photosynthesis, the light-independent reactions take place at:",
    "Biology", "Photosynthesis in Higher Plants", "Easy", "a",
    "Stromal matrix", "Thylakoid lumen", "Photosystem-I", "Photosystem-II")

add("Which of the following immunoglobulins constitutes the largest percentage in human milk?",
    "Biology", "Human Health and Disease", "Medium", "d",
    "IgG", "IgD", "IgM", "IgA")

add("Which of the following pairs is not correctly matched (mode of reproduction and example)?",
    "Biology", "Reproduction in Organisms", "Medium", "d",
    "Rhizome - Banana", "Binary fission - Sargassum", "Conidia - Penicillium", "Offset - Water hyacinth")

add("The UN conference of Parties on climate change in the year 2012 was held at:",
    "Biology", "Environmental Issues", "Easy", "c",
    "Warsaw", "Durban", "Doha", "Lima")

# ============ PHYSICS (136-180) ============

add("In the spectrum of hydrogen, the ratio of the longest wavelength in the Lyman series to the longest wavelength in the Balmer series is:",
    "Physics", "Atoms", "Medium", "a", "5/27", "4/9", "9/4", "27/5")

add("The energy of the em waves is of the order of 15 keV. To which part of the spectrum does it belong?",
    "Physics", "Electromagnetic Waves", "Medium", "b", "gamma-rays", "X-rays", "Infra-red rays", "Ultraviolet rays")

add("An electron moves on a straight line path XY as shown. The abcd is a coil adjacent to the path of electron. What will be the direction of current, if any, induced in the coil?",
    "Physics", "Electromagnetic Induction", "Hard", "d",
    "No current induced", "abcd", "adcb", "The current will reverse its direction as the electron goes past the coil")

add("The cylindrical tube of a spray pump has radius R, one end of which has n fine holes, each of radius r. If the speed of the liquid in the tube is V, the speed of the ejection of the liquid through the holes is:",
    "Physics", "Mechanical Properties of Fluids", "Medium", "c", "V^2R/(nr)", "VR^2/(n^2 r^2)", "VR^2/(nr^2)", "VR^2/(n^3 r^2)")

add("The Young's modulus of steel is twice that of brass. Two wires of same length and of same area of cross section, one of steel and another of brass are suspended from the same roof. If we want the lower ends of the wires to be at the same level, then the weights added to the steel and brass wires must be in the ratio of:",
    "Physics", "Mechanical Properties of Solids", "Medium", "c", "1:1", "1:2", "2:1", "4:2")

add("A potentiometer wire of length L and a resistance r are connected in series with a battery of e.m.f. E0 and a resistance r1. An unknown e.m.f. E is balanced at a length l of the potentiometer wire. The e.m.f. E will be given by:",
    "Physics", "Current Electricity", "Medium", "c",
    "L E0 r / [(r+r1) l]", "L E0 r / (l r1)", "E0 r / (r+r1) . (l/L)", "E0 l / L")

add("A particle is executing a simple harmonic motion. Its maximum acceleration is alpha and maximum velocity is beta. Then, its time period of vibration will be:",
    "Physics", "Oscillations", "Medium", "a", "2*pi*beta/alpha", "beta^2/alpha^2", "alpha/beta", "beta^2/alpha")

add("If vectors A = cos(wt) i + sin(wt) j and B = cos(wt/2) i + sin(wt/2) j are functions of time, then the value of t at which they are orthogonal to each other is:",
    "Physics", "Vectors / Motion in a Plane", "Medium", "d", "t=0", "t=pi/(4w)", "t=pi/(2w)", "t=pi/w")

add("A source of sound S emitting waves of frequency 100 Hz and an observer O are located at some distance from each other. The source is moving with a speed of 19.4 m/s at an angle of 60 degrees with the source-observer line. The observer is at rest. The apparent frequency observed by the observer (velocity of sound in air 330 m/s) is:",
    "Physics", "Waves", "Hard", "c", "97 Hz", "100 Hz", "103 Hz", "106 Hz")

add("An automobile moves on a road with a speed of 54 km/h. The radius of its wheels is 0.45 m and the moment of inertia of the wheel about its axis of rotation is 3 kg m^2. If the vehicle is brought to rest in 15 s, the magnitude of average torque transmitted by its brakes to the wheel is:",
    "Physics", "System of Particles and Rotational Motion", "Medium", "b",
    "2.86 kg m^2 s^-2", "6.66 kg m^2 s^-2", "8.58 kg m^2 s^-2", "10.86 kg m^2 s^-2")

add("A rectangular coil of length 0.12 m and width 0.1 m having 50 turns of wire is suspended vertically in a uniform magnetic field of strength 0.2 Weber/m^2. The coil carries a current of 2A. If the plane of the coil is inclined at an angle of 30 degrees with the direction of the field, the torque required to keep the coil in stable equilibrium will be:",
    "Physics", "Moving Charges and Magnetism", "Medium", "c", "0.12 Nm", "0.15 Nm", "0.20 Nm", "0.24 Nm")

add("A parallel plate air capacitor has capacity C, distance of separation between plates is d and potential difference V is applied between the plates. Force of attraction between the plates of the parallel plate air capacitor is:",
    "Physics", "Electrostatic Potential and Capacitance", "Medium", "c",
    "C^2 V^2 / (2 d^2)", "C^2 V^2 / (2 d)", "C V^2 / (2d)", "C V^2 / d")

add("Two vessels separately contain two ideal gases A and B at the same temperature, the pressure of A being twice that of B. Under such conditions, the density of A is found to be 1.5 times the density of B. The ratio of molecular weight of A and B is:",
    "Physics", "Kinetic Theory of Gases", "Medium", "c", "1/2", "2/3", "3/4", "2")

add("A satellite S is moving in an elliptical orbit around the earth. The mass of the satellite is very small compared to the mass of the earth. Then:",
    "Physics", "Gravitation", "Medium", "a",
    "The acceleration of S is always directed towards the centre of the earth",
    "The angular momentum of S about the centre of the earth changes in direction, but its magnitude remains constant",
    "The total mechanical energy of S varies periodically with time", "The linear momentum of S remains constant in magnitude")

add("In the given figure, a diode D is connected to an external resistance R = 100 ohm and an e.m.f. of 3.5 V. If the barrier potential developed across the diode is 0.5 V, the current in the circuit will be:",
    "Physics", "Semiconductor Electronics", "Easy", "b", "35 mA", "30 mA", "40 mA", "20 mA")

add("A remote-sensing satellite of earth revolves in a circular orbit at a height of 0.25x10^6 m above the surface of earth. If earth's radius is 6.38x10^6 m and g = 9.8 m/s^2, then the orbital speed of the satellite is:",
    "Physics", "Gravitation", "Medium", "b", "6.67 km/s", "7.76 km/s", "8.56 km/s", "9.13 km/s")

add("The position vector of a particle R as a function of time is given by R = 4 sin(2*pi*t) i + 4 cos(2*pi*t) j, where R is in meters, t is in seconds. Which one of the following statements is wrong for the motion of the particle?",
    "Physics", "Motion in a Plane", "Hard", "d",
    "Path of the particle is a circle of radius 4 meter", "Acceleration vector is along -R",
    "Magnitude of acceleration vector is v^2/R, where v is the velocity of particle",
    "Magnitude of the velocity of particle is 8 meter/second")

add("A string is stretched between fixed points separated by 75.0 cm. It is observed to have resonant frequencies of 420 Hz and 315 Hz. There is no other resonant frequency between 315 and 420 Hz. The lowest resonant frequency for this string is:",
    "Physics", "Waves", "Medium", "a", "105 Hz", "155 Hz", "205 Hz", "105 Hz")

add("Point masses m1 and m2 are placed at the opposite ends of a rigid rod of length L, and negligible mass. The rod is to be set rotating about an axis perpendicular to it. The position of point P on this rod through which the axis should pass so that the work required to set the rod rotating with angular velocity w0 is minimum, is given by:",
    "Physics", "System of Particles and Rotational Motion", "Hard", "a",
    "x = m2 L/(m1+m2)", "x = m1 L/(m1+m2)", "x = (m1/m2) L", "x = (m2/m1) L")

add("At the first minimum adjacent to the central maximum of a single-slit diffraction pattern, the phase difference between the Huygen's wavelet from the edge of the slit and the wavelet from the midpoint of the slit is:",
    "Physics", "Wave Optics", "Hard", "d", "pi/8 radian", "pi/4 radian", "pi/2 radian", "pi radian")

add("A force F = alpha*i + 3j + 6k is acting at a point r = 2i - 6j - 12k. The value of alpha for which angular momentum about origin is conserved is:",
    "Physics", "System of Particles and Rotational Motion", "Medium", "b", "1", "-1", "2", "Zero")

add("Two particles A and B move with constant velocities v1 and v2. At the initial moment their position vectors are r1 and r2 respectively. The condition for particles A and B for their collision is:",
    "Physics", "Motion in a Plane", "Hard", "b",
    "r1 x v1 = r2 x v2", "(r1-r2)/|r1-r2| = (v2-v1)/|v2-v1|", "r1.v1 = r2.v2", "r1 x v1 = r2 x v2 (duplicate)")

add("A nucleus of uranium decays at rest into nuclei of thorium and helium. Then:",
    "Physics", "Nuclei", "Medium", "b",
    "The helium nucleus has less kinetic energy than the thorium nucleus",
    "The helium nucleus has more kinetic energy than the thorium nucleus",
    "The helium nucleus has less momentum than the thorium nucleus",
    "The helium nucleus has more momentum than the thorium nucleus")

add("Two metal wires of identical dimensions are connected in series. If sigma1 and sigma2 are the conductivities of the metal wires respectively, the effective conductivity of the combination is:",
    "Physics", "Current Electricity", "Medium", "b",
    "sigma1 sigma2/(sigma1+sigma2)", "2 sigma1 sigma2/(sigma1+sigma2)",
    "(sigma1+sigma2)/(2 sigma1 sigma2)", "(sigma1+sigma2)/(sigma1 sigma2)")

add("Light of wavelength 500 nm is incident on a metal with work function 2.28 eV. The de Broglie wavelength of the emitted electron is:",
    "Physics", "Dual Nature of Radiation and Matter", "Hard", "d",
    "<= 2.8x10^-12 m", "< 2.8x10^-10 m", "< 2.8x10^-9 m", ">= 2.8x10^-9 m")

add("4.0 g of a gas occupies 22.4 litres at NTP. The specific heat capacity of the gas at constant volume is 5.0 J/K/mol. If the speed of sound in this gas at NTP is 952 m/s, then the heat capacity at constant pressure is (R = 8.3 J/K/mol):",
    "Physics", "Thermodynamics / Kinetic Theory", "Hard", "b",
    "8.5 J/K/mol", "8.0 J/K/mol", "7.5 J/K/mol", "7.0 J/K/mol")

add("A series R-C circuit is connected to an alternating voltage source. When capacitor is air filled vs mica filled, comparing current i through resistor and voltage V across capacitor, which relation holds?",
    "Physics", "Alternating Current", "Medium", "c",
    "Va = Vb", "Va < Vb", "Va > Vb", "ia > ib")

add("A plank with a box on it at one end is gradually raised about the other end. As the angle of inclination with the horizontal reaches 30 degrees, the box starts to slip and slides 4.0 m down the plank in 4.0 s. The coefficients of static and kinetic friction between the box and the plank will be, respectively:",
    "Physics", "Laws of Motion", "Medium", "c", "0.4 and 0.3", "0.6 and 0.6", "0.6 and 0.5", "0.5 and 0.6")

add("Two stones of masses m and 2m are whirled in horizontal circles, the heavier one in a radius r/2 and the lighter one in radius r. The tangential speed of lighter stone is n times that of the value of heavier stone when they experience same centripetal forces. The value of n is:",
    "Physics", "Circular Motion / Laws of Motion", "Medium", "b", "1", "2", "3", "4")

add("The coefficient of performance of a refrigerator is 5. If the temperature inside freezer is -20 degree C, the temperature of the surrounding to which it rejects heat is:",
    "Physics", "Thermodynamics", "Medium", "b", "21 C", "31 C", "41 C", "11 C")

add("An ideal gas is compressed to half its initial volume by means of several processes. Which of the processes results in the maximum work done on the gas?",
    "Physics", "Thermodynamics", "Medium", "b", "Isothermal", "Adiabatic", "Isobaric", "Isochoric")

add("A ball is thrown vertically downwards from a height of 20 m with an initial velocity v0. It collides with the ground, loses 50 percent of its energy in collision and rebounds to the same height. The initial velocity v0 is: (g=10 m/s^2)",
    "Physics", "Motion in a Straight Line", "Medium", "c", "10 m/s", "14 m/s", "20 m/s", "28 m/s")

add("On a frictionless surface, a block of mass M moving at speed v collides elastically with another block of same mass M which is initially at rest. After collision the first block moves at an angle theta to its initial direction and has a speed v/3. The second block's speed after the collision is:",
    "Physics", "Work, Energy and Power", "Hard", "b", "(sqrt3/2) v", "(2 sqrt2/3) v", "(3/4) v", "(3/sqrt2) v")

add("If potential (in volts) in a region is expressed as V(x,y,z) = 6xy - y + 2yz, the electric field (in N/C) at point (1,1,0) is:",
    "Physics", "Electrostatic Potential and Capacitance", "Medium", "c",
    "-(6i+9j+k)", "-(3i+5j+3k)", "-(6i+5j+2k)", "-(2i+3j+k)")

add("Two slits in Young's experiment have widths in the ratio 1:25. The ratio of intensity at the maxima and minima in the interference pattern, Imax/Imin, is:",
    "Physics", "Wave Optics", "Medium", "b", "4/9", "9/4", "121/49", "49/121")

add("The heart of a man pumps 5 litres of blood through the arteries per minute at a pressure of 150 mm of mercury. If the density of mercury be 13.6x10^3 kg/m^3 and g=10 m/s^2, then the power of heart in watt is:",
    "Physics", "Mechanical Properties of Fluids", "Medium", "b", "1.50", "1.70", "2.35", "3.0")

add("A proton and an alpha particle both enter a region of uniform magnetic field B, moving at right angles to the field B. If the radius of circular orbits for both the particles is equal and the kinetic energy acquired by proton is 1 MeV, the energy acquired by the alpha particle will be:",
    "Physics", "Moving Charges and Magnetism", "Medium", "a", "1 MeV", "4 MeV", "0.5 MeV", "1.5 MeV")

add("The input signal given to a CE amplifier having a voltage gain of 150 is Vi = 2 cos(15t + pi/3). The corresponding output signal will be:",
    "Physics", "Semiconductor Electronics", "Medium", "a",
    "300 cos(15t + 4pi/3)", "300 cos(15t + pi/3)", "75 cos(15t + 2pi/3)", "2 cos(15t + 5pi/6)")

add("If dimensions of critical velocity vc of a liquid flowing through a tube are expressed as [eta^x rho^y r^z], where eta, rho and r are the coefficient of viscosity of liquid, density of liquid and radius of the tube respectively, then the values of x, y and z are given by:",
    "Physics", "Mechanical Properties of Fluids / Units and Dimensions", "Medium", "b",
    "1, 1, 1", "1, -1, -1", "-1, -1, 1", "-1, -1, -1")

add("A circuit contains an ammeter, a battery of 30 V and a resistance 40.8 ohm all connected in series. If the ammeter has a coil of resistance 480 ohm and a shunt of 20 ohm, the reading in the ammeter will be:",
    "Physics", "Current Electricity", "Medium", "b", "1 A", "0.5 A", "0.25 A", "2 A")

add("Water rises to a height h in a capillary tube. If the length of capillary tube above the surface of water is made less than h, then:",
    "Physics", "Mechanical Properties of Fluids", "Medium", "c",
    "Water does not rise at all", "Water rises upto the tip of capillary tube and then starts overflowing like a fountain",
    "Water rises upto the top of capillary tube and stays there without overflowing",
    "Water rises upto a point a little below the top and stays there")

add("In an astronomical telescope in normal adjustment a straight black line of length L is drawn on the inside part of the objective lens. The eye-piece forms a real image of this line, of length I. The magnification of the telescope is:",
    "Physics", "Ray Optics and Optical Instruments", "Hard", "a", "L/I", "L/I + 1", "L/I - 1", "(L+I)/(L-I)")

add("The value of coefficient of volume expansion of glycerin is 5x10^-4 K^-1. The fractional change in the density of glycerin for a rise of 40 degree C in its temperature is:",
    "Physics", "Thermal Properties of Matter", "Medium", "c", "0.010", "0.015", "0.020", "0.025")

add("A photoelectric surface is illuminated successively by monochromatic light of wavelength lambda and lambda/2. If the maximum kinetic energy of the emitted photoelectrons in the second case is 3 times that in the first case, the work function of the surface of the material is: (h=Planck's constant, c=speed of light)",
    "Physics", "Dual Nature of Radiation and Matter", "Hard", "b", "hc/(3*lambda)", "hc/(2*lambda)", "hc/lambda", "2hc/lambda")

add("A beam of light consisting of red, green and blue colours is incident on a right angled prism (45-45-90). The refractive indices of the prism material for red, green and blue wavelengths are 1.39, 1.44 and 1.47 respectively. The prism will:",
    "Physics", "Ray Optics and Optical Instruments", "Hard", "a",
    "Separate the red colour part from the green and blue colours",
    "Separate the blue colour part from the red and green colours",
    "Separate all the three colours from one another", "Not separate the three colours at all")

# Write CSV
with open("/home/claude/neet_2015_code_a.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["questions","subject","chapter","difficulty","answer",
                                            "option_a","option_b","option_c","option_d","year"])
    writer.writeheader()
    for r in rows:
        writer.writerow(r)

print("Total questions written:", len(rows))