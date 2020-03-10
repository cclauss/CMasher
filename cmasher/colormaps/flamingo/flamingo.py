from matplotlib.colors import ListedColormap

cm_type = "linear"

cm_data = [[0.00000000e+00, 0.00000000e+00, 0.00000000e+00],
           [3.20937993e-04, 2.05053732e-04, 1.87624915e-04],
           [1.15420360e-03, 6.98088053e-04, 6.31313077e-04],
           [2.46983383e-03, 1.42160483e-03, 1.27199902e-03],
           [4.26478339e-03, 2.34745685e-03, 2.08029107e-03],
           [6.54250799e-03, 3.45656417e-03, 3.03628261e-03],
           [9.30925288e-03, 4.73442301e-03, 4.12495818e-03],
           [1.25724716e-02, 6.16937441e-03, 5.33442254e-03],
           [1.63410077e-02, 7.75142091e-03, 6.65457751e-03],
           [2.06234969e-02, 9.47213093e-03, 8.07714365e-03],
           [2.54300751e-02, 1.13236698e-02, 9.59446233e-03],
           [3.07698598e-02, 1.32993925e-02, 1.12003234e-02],
           [3.66537602e-02, 1.53927146e-02, 1.28885413e-02],
           [4.29990713e-02, 1.75980690e-02, 1.46541956e-02],
           [4.93444288e-02, 1.99097294e-02, 1.64921659e-02],
           [5.56518828e-02, 2.23227453e-02, 1.83983054e-02],
           [6.19271740e-02, 2.48321185e-02, 2.03684328e-02],
           [6.81750508e-02, 2.74331329e-02, 2.23987465e-02],
           [7.43990450e-02, 3.01215566e-02, 2.44860551e-02],
           [8.06036939e-02, 3.28925287e-02, 2.66264884e-02],
           [8.67908230e-02, 3.57425540e-02, 2.88178001e-02],
           [9.29644460e-02, 3.86668145e-02, 3.10562942e-02],
           [9.91261438e-02, 4.16312219e-02, 3.33398661e-02],
           [1.05278143e-01, 4.45292542e-02, 3.56659845e-02],
           [1.11423294e-01, 4.73693950e-02, 3.80315787e-02],
           [1.17562269e-01, 5.01543883e-02, 4.04352730e-02],
           [1.23697366e-01, 5.28855751e-02, 4.27932640e-02],
           [1.29830254e-01, 5.55644290e-02, 4.51046059e-02],
           [1.35961586e-01, 5.81928911e-02, 4.73720526e-02],
           [1.42093184e-01, 6.07718621e-02, 4.95969380e-02],
           [1.48226484e-01, 6.33023047e-02, 5.17807119e-02],
           [1.54361866e-01, 6.57857731e-02, 5.39255285e-02],
           [1.60500389e-01, 6.82231745e-02, 5.60328112e-02],
           [1.66644104e-01, 7.06145162e-02, 5.81030052e-02],
           [1.72792886e-01, 7.29612988e-02, 6.01382555e-02],
           [1.78947577e-01, 7.52641864e-02, 6.21397789e-02],
           [1.85109008e-01, 7.75237382e-02, 6.41086976e-02],
           [1.91278732e-01, 7.97398289e-02, 6.60454262e-02],
           [1.97456798e-01, 8.19134194e-02, 6.79515666e-02],
           [2.03643792e-01, 8.40449681e-02, 6.98281921e-02],
           [2.09840386e-01, 8.61347794e-02, 7.16762321e-02],
           [2.16047221e-01, 8.81831032e-02, 7.34965796e-02],
           [2.22265052e-01, 9.01900155e-02, 7.52899732e-02],
           [2.28494716e-01, 9.21554424e-02, 7.70570292e-02],
           [2.34736316e-01, 9.40798739e-02, 7.87989444e-02],
           [2.40990384e-01, 9.59633718e-02, 8.05165057e-02],
           [2.47257433e-01, 9.78059556e-02, 8.22104808e-02],
           [2.53537954e-01, 9.96076039e-02, 8.38816213e-02],
           [2.59832418e-01, 1.01368256e-01, 8.55306653e-02],
           [2.66141277e-01, 1.03087813e-01, 8.71583403e-02],
           [2.72464964e-01, 1.04766141e-01, 8.87653649e-02],
           [2.78803897e-01, 1.06403068e-01, 9.03524520e-02],
           [2.85158475e-01, 1.07998388e-01, 9.19203106e-02],
           [2.91529081e-01, 1.09551862e-01, 9.34696480e-02],
           [2.97916083e-01, 1.11063218e-01, 9.50011723e-02],
           [3.04319831e-01, 1.12532151e-01, 9.65155944e-02],
           [3.10740661e-01, 1.13958324e-01, 9.80136298e-02],
           [3.17178894e-01, 1.15341369e-01, 9.94960012e-02],
           [3.23634860e-01, 1.16680862e-01, 1.00963419e-01],
           [3.30109538e-01, 1.17975637e-01, 1.02416048e-01],
           [3.36602587e-01, 1.19225869e-01, 1.03855164e-01],
           [3.43114264e-01, 1.20431063e-01, 1.05281536e-01],
           [3.49644814e-01, 1.21590695e-01, 1.06695955e-01],
           [3.56194799e-01, 1.22703836e-01, 1.08098951e-01],
           [3.62765033e-01, 1.23769196e-01, 1.09490861e-01],
           [3.69354881e-01, 1.24787078e-01, 1.10873227e-01],
           [3.75964575e-01, 1.25756770e-01, 1.12246885e-01],
           [3.82595794e-01, 1.26675780e-01, 1.13611512e-01],
           [3.89247216e-01, 1.27545090e-01, 1.14969250e-01],
           [3.95919842e-01, 1.28362877e-01, 1.16320368e-01],
           [4.02614027e-01, 1.29128007e-01, 1.17665690e-01],
           [4.09329438e-01, 1.29840140e-01, 1.19006613e-01],
           [4.16067218e-01, 1.30497010e-01, 1.20343391e-01],
           [4.22826731e-01, 1.31098527e-01, 1.21677717e-01],
           [4.29608766e-01, 1.31642703e-01, 1.23010199e-01],
           [4.36413555e-01, 1.32128167e-01, 1.24341925e-01],
           [4.43240597e-01, 1.32554465e-01, 1.25674586e-01],
           [4.50091370e-01, 1.32918345e-01, 1.27008407e-01],
           [4.56965285e-01, 1.33219277e-01, 1.28345246e-01],
           [4.63862404e-01, 1.33455751e-01, 1.29686516e-01],
           [4.70783052e-01, 1.33625763e-01, 1.31033494e-01],
           [4.77727743e-01, 1.33726892e-01, 1.32387393e-01],
           [4.84696724e-01, 1.33756945e-01, 1.33749706e-01],
           [4.91689820e-01, 1.33714231e-01, 1.35122308e-01],
           [4.98707215e-01, 1.33596364e-01, 1.36506906e-01],
           [5.05749045e-01, 1.33400858e-01, 1.37905339e-01],
           [5.12815438e-01, 1.33125046e-01, 1.39319561e-01],
           [5.19907099e-01, 1.32765078e-01, 1.40751272e-01],
           [5.27023510e-01, 1.32318895e-01, 1.42203124e-01],
           [5.34164552e-01, 1.31783570e-01, 1.43677641e-01],
           [5.41330415e-01, 1.31155367e-01, 1.45177309e-01],
           [5.48521888e-01, 1.30429111e-01, 1.46704449e-01],
           [5.55737527e-01, 1.29603369e-01, 1.48262952e-01],
           [5.62978929e-01, 1.28670688e-01, 1.49855118e-01],
           [5.70244699e-01, 1.27628816e-01, 1.51485278e-01],
           [5.77534835e-01, 1.26472434e-01, 1.53157232e-01],
           [5.84849601e-01, 1.25195096e-01, 1.54874999e-01],
           [5.92188564e-01, 1.23791137e-01, 1.56643371e-01],
           [5.99550972e-01, 1.22254935e-01, 1.58467735e-01],
           [6.06936886e-01, 1.20578319e-01, 1.60353615e-01],
           [6.14345134e-01, 1.18754968e-01, 1.62307711e-01],
           [6.21774278e-01, 1.16778352e-01, 1.64337487e-01],
           [6.29224581e-01, 1.14636674e-01, 1.66450603e-01],
           [6.36693369e-01, 1.12324051e-01, 1.68656806e-01],
           [6.44179325e-01, 1.09829890e-01, 1.70966515e-01],
           [6.51680309e-01, 1.07144062e-01, 1.73391868e-01],
           [6.59193134e-01, 1.04257579e-01, 1.75947004e-01],
           [6.66714112e-01, 1.01161053e-01, 1.78648283e-01],
           [6.74238310e-01, 9.78468655e-02, 1.81514911e-01],
           [6.81759930e-01, 9.43081013e-02, 1.84569564e-01],
           [6.89270327e-01, 9.05456366e-02, 1.87839252e-01],
           [6.96758138e-01, 8.65694686e-02, 1.91356123e-01],
           [7.04208704e-01, 8.24032624e-02, 1.95158707e-01],
           [7.11601491e-01, 7.80990541e-02, 1.99292760e-01],
           [7.18909192e-01, 7.37495289e-02, 2.03812305e-01],
           [7.26093608e-01, 6.95201000e-02, 2.08778032e-01],
           [7.33104912e-01, 6.56726552e-02, 2.14254745e-01],
           [7.39878375e-01, 6.26044236e-02, 2.20299557e-01],
           [7.46339501e-01, 6.08296655e-02, 2.26945910e-01],
           [7.52414614e-01, 6.08878421e-02, 2.34179342e-01],
           [7.58050571e-01, 6.31462987e-02, 2.41924975e-01],
           [7.63230997e-01, 6.76279846e-02, 2.50058577e-01],
           [7.67977797e-01, 7.40146683e-02, 2.58440612e-01],
           [7.72337710e-01, 8.18169694e-02, 2.66949754e-01],
           [7.76365757e-01, 9.05539133e-02, 2.75496613e-01],
           [7.80113613e-01, 9.98450862e-02, 2.84024596e-01],
           [7.83625590e-01, 1.09422381e-01, 2.92498875e-01],
           [7.86937105e-01, 1.19111259e-01, 3.00901754e-01],
           [7.90076674e-01, 1.28801487e-01, 3.09223443e-01],
           [7.93066614e-01, 1.38427032e-01, 3.17460501e-01],
           [7.95924415e-01, 1.47950263e-01, 3.25613033e-01],
           [7.98664468e-01, 1.57350207e-01, 3.33681878e-01],
           [8.01297984e-01, 1.66617931e-01, 3.41669762e-01],
           [8.03834621e-01, 1.75750223e-01, 3.49578786e-01],
           [8.06281888e-01, 1.84749074e-01, 3.57412181e-01],
           [8.08646510e-01, 1.93618015e-01, 3.65172311e-01],
           [8.10933833e-01, 2.02362658e-01, 3.72862075e-01],
           [8.13148706e-01, 2.10988790e-01, 3.80483745e-01],
           [8.15295226e-01, 2.19502685e-01, 3.88039612e-01],
           [8.17376884e-01, 2.27910757e-01, 3.95531914e-01],
           [8.19397360e-01, 2.36218353e-01, 4.02961911e-01],
           [8.21358911e-01, 2.44432195e-01, 4.10332139e-01],
           [8.23264666e-01, 2.52557007e-01, 4.17643491e-01],
           [8.25116507e-01, 2.60598634e-01, 4.24897987e-01],
           [8.26916729e-01, 2.68561725e-01, 4.32096767e-01],
           [8.28667536e-01, 2.76450534e-01, 4.39240800e-01],
           [8.30370618e-01, 2.84269497e-01, 4.46331378e-01],
           [8.32027646e-01, 2.92022614e-01, 4.53369584e-01],
           [8.33640283e-01, 2.99713487e-01, 4.60356313e-01],
           [8.35210220e-01, 3.07345342e-01, 4.67292290e-01],
           [8.36738724e-01, 3.14921563e-01, 4.74178514e-01],
           [8.38227122e-01, 3.22445163e-01, 4.81015795e-01],
           [8.39676722e-01, 3.29918901e-01, 4.87804850e-01],
           [8.41089270e-01, 3.37344834e-01, 4.94545935e-01],
           [8.42465402e-01, 3.44725986e-01, 5.01240194e-01],
           [8.43806740e-01, 3.52064134e-01, 5.07887852e-01],
           [8.45114179e-01, 3.59361633e-01, 5.14489687e-01],
           [8.46389111e-01, 3.66620167e-01, 5.21046021e-01],
           [8.47632288e-01, 3.73841904e-01, 5.27557630e-01],
           [8.48845360e-01, 3.81028006e-01, 5.34024572e-01],
           [8.50028886e-01, 3.88180557e-01, 5.40447682e-01],
           [8.51184035e-01, 3.95300937e-01, 5.46827308e-01],
           [8.52312175e-01, 4.02390259e-01, 5.53163650e-01],
           [8.53413995e-01, 4.09450151e-01, 5.59457346e-01],
           [8.54490552e-01, 4.16481819e-01, 5.65708760e-01],
           [8.55542889e-01, 4.23486404e-01, 5.71918250e-01],
           [8.56572188e-01, 4.30464859e-01, 5.78086076e-01],
           [8.57579325e-01, 4.37418334e-01, 5.84212678e-01],
           [8.58565259e-01, 4.44347837e-01, 5.90298425e-01],
           [8.59530998e-01, 4.51254287e-01, 5.96343650e-01],
           [8.60477541e-01, 4.58138554e-01, 6.02348681e-01],
           [8.61405886e-01, 4.65001464e-01, 6.08313844e-01],
           [8.62317027e-01, 4.71843802e-01, 6.14239458e-01],
           [8.63211957e-01, 4.78666313e-01, 6.20125838e-01],
           [8.64091670e-01, 4.85469706e-01, 6.25973296e-01],
           [8.64957160e-01, 4.92254655e-01, 6.31782138e-01],
           [8.65809424e-01, 4.99021801e-01, 6.37552667e-01],
           [8.66649463e-01, 5.05771754e-01, 6.43285183e-01],
           [8.67478281e-01, 5.12505095e-01, 6.48979982e-01],
           [8.68296886e-01, 5.19222378e-01, 6.54637356e-01],
           [8.69106293e-01, 5.25924129e-01, 6.60257593e-01],
           [8.69907523e-01, 5.32610853e-01, 6.65840980e-01],
           [8.70701602e-01, 5.39283028e-01, 6.71387799e-01],
           [8.71489566e-01, 5.45941112e-01, 6.76898330e-01],
           [8.72272465e-01, 5.52585538e-01, 6.82372849e-01],
           [8.73051401e-01, 5.59216690e-01, 6.87811613e-01],
           [8.73827370e-01, 5.65835009e-01, 6.93214917e-01],
           [8.74601443e-01, 5.72440876e-01, 6.98583029e-01],
           [8.75374698e-01, 5.79034655e-01, 7.03916216e-01],
           [8.76148226e-01, 5.85616694e-01, 7.09214743e-01],
           [8.76923129e-01, 5.92187327e-01, 7.14478871e-01],
           [8.77700526e-01, 5.98746866e-01, 7.19708858e-01],
           [8.78481568e-01, 6.05295601e-01, 7.24904957e-01],
           [8.79267347e-01, 6.11833850e-01, 7.30067434e-01],
           [8.80059016e-01, 6.18361889e-01, 7.35196540e-01],
           [8.80857737e-01, 6.24879984e-01, 7.40292526e-01],
           [8.81664690e-01, 6.31388387e-01, 7.45355640e-01],
           [8.82481071e-01, 6.37887338e-01, 7.50386127e-01],
           [8.83308082e-01, 6.44377071e-01, 7.55384232e-01],
           [8.84146936e-01, 6.50857809e-01, 7.60350198e-01],
           [8.84998875e-01, 6.57329761e-01, 7.65284263e-01],
           [8.85865154e-01, 6.63793123e-01, 7.70186664e-01],
           [8.86747050e-01, 6.70248084e-01, 7.75057635e-01],
           [8.87645836e-01, 6.76694828e-01, 7.79897411e-01],
           [8.88562825e-01, 6.83133523e-01, 7.84706221e-01],
           [8.89499358e-01, 6.89564319e-01, 7.89484291e-01],
           [8.90456786e-01, 6.95987363e-01, 7.94231847e-01],
           [8.91436484e-01, 7.02402788e-01, 7.98949113e-01],
           [8.92439850e-01, 7.08810721e-01, 8.03636311e-01],
           [8.93468266e-01, 7.15211293e-01, 8.08293661e-01],
           [8.94523192e-01, 7.21604602e-01, 8.12921379e-01],
           [8.95606115e-01, 7.27990730e-01, 8.17519682e-01],
           [8.96718532e-01, 7.34369758e-01, 8.22088785e-01],
           [8.97861971e-01, 7.40741755e-01, 8.26628900e-01],
           [8.99037988e-01, 7.47106778e-01, 8.31140242e-01],
           [9.00248171e-01, 7.53464870e-01, 8.35623023e-01],
           [9.01494140e-01, 7.59816062e-01, 8.40077453e-01],
           [9.02777503e-01, 7.66160395e-01, 8.44503743e-01],
           [9.04100007e-01, 7.72497844e-01, 8.48902108e-01],
           [9.05463389e-01, 7.78828393e-01, 8.53272762e-01],
           [9.06869428e-01, 7.85152009e-01, 8.57615922e-01],
           [9.08319953e-01, 7.91468642e-01, 8.61931808e-01],
           [9.09816838e-01, 7.97778221e-01, 8.66220645e-01],
           [9.11362014e-01, 8.04080652e-01, 8.70482661e-01],
           [9.12957472e-01, 8.10375820e-01, 8.74718094e-01],
           [9.14605265e-01, 8.16663582e-01, 8.78927188e-01],
           [9.16307518e-01, 8.22943768e-01, 8.83110201e-01],
           [9.18066432e-01, 8.29216176e-01, 8.87267405e-01],
           [9.19884297e-01, 8.35480568e-01, 8.91399088e-01],
           [9.21763494e-01, 8.41736668e-01, 8.95505561e-01],
           [9.23706513e-01, 8.47984152e-01, 8.99587164e-01],
           [9.25715965e-01, 8.54222651e-01, 9.03644274e-01],
           [9.27794593e-01, 8.60451734e-01, 9.07677311e-01],
           [9.29945295e-01, 8.66670906e-01, 9.11686754e-01],
           [9.32171105e-01, 8.72879614e-01, 9.15673149e-01],
           [9.34475267e-01, 8.79077209e-01, 9.19637138e-01],
           [9.36861324e-01, 8.85262908e-01, 9.23579524e-01],
           [9.39333022e-01, 8.91435833e-01, 9.27501272e-01],
           [9.41894393e-01, 8.97594970e-01, 9.31403583e-01],
           [9.44549779e-01, 9.03739150e-01, 9.35287990e-01],
           [9.47303747e-01, 9.09867077e-01, 9.39156422e-01],
           [9.50161360e-01, 9.15977183e-01, 9.43011527e-01],
           [9.53127907e-01, 9.22067725e-01, 9.46856824e-01],
           [9.56208739e-01, 9.28136815e-01, 9.50697060e-01],
           [9.59408812e-01, 9.34182557e-01, 9.54538605e-01],
           [9.62732463e-01, 9.40203047e-01, 9.58390330e-01],
           [9.66181773e-01, 9.46196978e-01, 9.62263999e-01],
           [9.69754665e-01, 9.52164352e-01, 9.66174709e-01],
           [9.73442608e-01, 9.58107370e-01, 9.70140927e-01],
           [9.77227055e-01, 9.64032066e-01, 9.74182187e-01],
           [9.81077719e-01, 9.69949414e-01, 9.78314679e-01],
           [9.84954316e-01, 9.75875300e-01, 9.82544391e-01],
           [9.88813264e-01, 9.81828491e-01, 9.86860615e-01],
           [9.92618443e-01, 9.87826429e-01, 9.91235239e-01],
           [9.96348727e-01, 9.93881649e-01, 9.95628664e-01],
           [1.00000000e+00, 1.00000000e+00, 1.00000000e+00]]

test_cm = ListedColormap(cm_data, name="flamingo")
