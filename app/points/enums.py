import enum


class StatusEnum(str, enum.Enum):
    PUBLISHED = "опубликован"
    DELETED = "удален"
    UNDER_MODERATION = "на модерации"
    DRAFT = "черновик"
    SCHEDULED = "отложенная публикация"


class FishEnum(str, enum.Enum):
    grass_carp = "амур белый"
    black_carp = "амур чёрный"
    white_eye_bream = "белоглазка"
    beloribitsa_whitefish = "белорыбица"
    beluga = "белуга каспийская"
    black_sea_beluga = "белуга черноморская"
    volga_zander = "берш"
    buffalo = "буффало большеротый"
    black_buffalo = "буффало чёрный"
    round_whitefish = "валёк"
    caspian_roach = "вобла"
    black_sea_kutum = "вырезуб"
    loach = "вьюн"
    chub = "голавль"
    arctic_char = "голец арктический"
    dryagin_char = "голец дрягина"
    kuori_char = "голец куорский"
    levanidovs_char = "голец леванидова"
    siberian_char_loach = "голец сибирский-усач"
    common_minnow = "гольян"
    lake_minnow = "гольян озёрный"
    pink_salmon = "горбуша"
    white_bream = "густера"
    zebra_mussel = "дрейссена речная"
    dace = "елец"
    siberian_dace = "елец сибирский"
    ruffe = "ёрш"
    donets_ruffe = "ёрш-носарь"
    asp = "жерех"
    kaluga = "калуга"
    crucian_carp = "карась золотой"
    gibel_carp = "карась серебряный"
    leather_carp = "карп голый"
    scaleless_albino_carp = "карп голый - альбинос"
    scaleless_ghost_carp = "карп голый - призрак"
    mirror_carp = "карп зеркальный"
    mirror_albino_carp = "карп зеркальный - альбинос"
    mirror_ghost_carp = "карп зеркальный - призрак"
    starvas_red_carp_mirror = "карп красный старвас - зеркальный"
    red_starvas_carp_scaly = "карп красный старвас - чешуйчатый"
    linear_carp = "карп линейный"
    linear_albino_carp = "карп линейный - альбинос"
    linear_ghost_carp = "карп линейный - призрак"
    frame_sided_carp = "карп рамчатый"
    frame_sided_albino_carp = "карп рамчатый - альбинос"
    frame_sided_ghost_carp = "карп рамчатый - призрак"
    common_carp = "карп чешуйчатый"
    common_scaly_albino_carp = "карп чешуйчатый - альбинос"
    common_ghost_carp = "карп чешуйчатый - призрак"
    chum_salmon = "кета"
    coho_salmon = "кижуч"
    nine_spined_stickleback = "колюшка девятииглая"
    small_southern_stickleback = "колюшка малая южная"
    three_spined_stickleback = "колюшка трёхиглая"
    smelt = "корюшка"
    asian_smelt = "корюшка азиатская"
    rudd = "краснопёрка"
    whitespotted_char = "кунджа"
    caspian_kutum = "кутум"
    sharp_snouted_lenok = "ленок острорылый"
    bream = "лещ"
    eastern_bream = "лещ восточный"
    tench = "линь"
    golden_tench = "линь золотистый"
    atlantic_salmon = "лосось атлантический"
    caspian_brown_trout = "лосось каспийский"
    ladoga_salmon = "лосось ладожский"
    frog = "лягушка"
    dolly_varden_trout = "мальма"
    kamchatkan_rainbow_trout = "микижа"
    far_eastern_brook_lamprey = "минога дальневосточная ручьевая"
    caspian_lamprey = "минога каспийская"
    siberian_lamprey = "минога сибирская"
    three_toothed_lamprey = "минога трёхзубая"
    ukrainian_lamprey = "минога украинская"
    muksun = "муксун"
    burbot = "налим"
    neiva = "нейва"
    nelma = "нельма"
    sockeye_salmon = "нерка"
    perch = "окунь"
    pumpkinseed_sunfish = "окунь солнечный"
    arctic_omul = "омуль арктический"
    baikal_omul = "омуль байкальский"
    baltic_sturgeon = "осётр балтийский"
    east_siberian_sturgeon = "осётр восточносибирский"
    ladoga_sturgeon = "осётр ладожский"
    persian_sturgeon = "осётр персидский"
    russian_sturgeon = "осётр русский"
    gray_char = "палия кряжевая"
    red_char = "палия лудожная"
    char = "палия обыкновенная"
    peled = "пелядь"
    river_mussel = "перловица"
    gudgeon = "пескарь обыкновенный"
    siberian_gudgeon = "пескарь сибирский"
    common_roach = "плотва обыкновенная"
    siberian_roach = "плотва сибирская"
    siberian_sculpin = "подкаменщик сибирский"
    silver_bream = "подлещик"
    nase = "подуст"
    black_spined_herring = "пузанок каспийский"
    freshwater_crayfish = "рак речной"
    ripus = "рипус"
    chinese_sleeper = "ротан"
    vimba = "рыбец"
    vendace = "ряпушка"
    siberian_sardine_cisco = "ряпушка сибирская"
    wild_carp = "сазан"
    stellate_sturgeon = "севрюга"
    brazhnikov_herring = "сельдь бражникова"
    kesslers_herring = "сельдь кесслера"
    pontic_shad = "сельдь черноморская"
    valaam_whitefish = "сиг валаамский"
    volkhov_whitefish = "сиг волховский"
    vuoksa_whitefish = "сиг вуоксинский"
    kuori_whitefish = "сиг куорский"
    ladoga_lake_whitefish = "сиг ладожский озёрный"
    svir_whitefish = "сиг свирский"
    black_whitefish = "сиг чёрный"
    ludoga_whitefish = "сиг-лудога"
    humpback_whitefish = "сиг-пыжьян"
    blue_bream = "синец"
    catfish = "сом"
    albino_catfish = "сом альбинос"
    amur_catfish = "сом амурский"
    sterlet = "стерлядь"
    siberian_sterlet = "стерлядь сибирская"
    zander = "судак"
    taimen = "таймень"
    taran = "тарань"
    silver_carp = "толстолобик белый"
    bighead_carp = "толстолобик пёстрый"
    tugun = "тугун"
    clupeonella = "тюлька черноморская"
    eel = "угорь"
    bleak = "уклейка"
    short_headed_barbel = "усач короткоголовый"
    common_barbel = "усач обыкновенный"
    lake_trout = "форель озерная"
    rainbow_trout = "форель радужная"
    brown_trout = "форель ручьевая"
    sevan_trout = "форель севанская"
    east_siberian_grayling = "хариус восточносибирский"
    grayling = "хариус европейский"
    arctic_grayling = "хариус западносибирский"
    chinook_salmon = "чавыча"
    sichel = "чехонь"
    broad_whitefish = "чир"
    longnose_sucker = "чукучан"
    shemaya = "шемая каспийская"
    black_sea_shemaya = "шемая черноморская"
    bastard_sturgeon = "шип"
    pike = "щука обыкновенная"
    ide = "язь"


class LocationEnum(str, enum.Enum):
    the_cottage_pond = "дачный пруд"
    mosquito_lake = "оз. комариное"
    winding_rivulet = "р. вьюнок"
    old_burg_lake = "оз. старый острог"
    belaya_river = "р. белая"
    kuori_lake = "оз. куори"
    bear_lake = "оз. медвежье"
    sura_river = "р. сура"
    volkhov_river = "р. волхов"
    ladoga_lake = "оз. ладожское"
    akhtuba_river = "р. ахтуба"
    the_amber_lake = "оз. янтарное"
    seversky_donets_river = "р. северский донец"
    lower_tunguska_river = "р. нижняя тунгуска"
    yama_river = "р. яма"
    ladoga_archipelago = "ладожский архипелаг"
