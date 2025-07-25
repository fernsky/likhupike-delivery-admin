from django.core.management.base import BaseCommand
from django.utils.text import slugify
from apps.reports.models import ReportCategory, ReportSection


class Command(BaseCommand):
    help = "Populate the database with Introduction chapter content for likhupike Rural Municipality"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Force update existing sections with new content",
        )

    def handle(self, *args, **options):
        force_update = options["force"]
        self.stdout.write(
            self.style.SUCCESS("Starting to populate Introduction chapter...")
        )

        if force_update:
            self.stdout.write(
                self.style.WARNING(
                    "Force update mode enabled - will update existing sections"
                )
            )

        # Create the Introduction category
        category, created = ReportCategory.objects.get_or_create(
            slug="introduction",
            defaults={
                "name": "Introduction",
                "name_nepali": "परिचय",
                "category_number": "१",
                "description": "Introduction chapter covering background, objectives, legal framework, methodology, and scope",
                "description_nepali": "पृष्ठभूमि, उद्देश्य, कानूनी ढाँचा, कार्यविधि र क्षेत्र समेट्ने परिचय अध्याय",
                "order": 1,
                "icon": "fas fa-book-open",
                "is_active": True,
            },
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f"Created category: {category.name}"))
        else:
            self.stdout.write(
                self.style.WARNING(f"Category already exists: {category.name}")
            )
            if force_update:
                # Update category_number if force update
                category.category_number = "१"
                category.name_nepali = "परिचय"
                category.save()
                self.stdout.write(
                    self.style.SUCCESS(f"Updated category number for: {category.name}")
                )

        # Define all sections with their content - using exact format from provided text
        sections_data = [
            {
                "section_number": "१.१",
                "title": "Background",
                "title_nepali": "पृष्ठभूमि",
                "slug": "background",
                "content_nepali": """<p>नेपाली जनताको बलिदानपूर्ण लामो संघर्षपछि नेपालमा संघीय लोकतान्त्रिक गणतन्त्रात्मक राज्य व्यवस्था कायम भएको छ । विश्वभर विभिन्न देशहरूमा सफल अभ्यासमा आएको यो व्यवस्था नेपालमा नौलो भएकाले यसमा अभ्यस्त हुन केही समय अवश्य लाग्नेछ । संघीय शासन प्रणालीको सवल पक्ष भनेको जनता केन्द्रीत शासन हो । नेपालको संघीय शासन प्रणाली अन्र्तगत राज्यको संरचनालाई तीन तहमा विभाजन गरिएको छ । संघीय अर्थात केन्द्रीय शासन, प्रादेशिक शासन बीचमा र तल्लो तहमा स्थानीय सरकार सरह नेपालको संविधानले स्थानीय तहहरूलाई स्थानीय स्वायत्त सरकारको रुपमा स्थापित गरेको छ । संविधानको अनुसूची ८ को क्र.सं. ६ मा स्थानीय तथ्याङ्क र अभिलेख संकलन सम्बन्धी सम्पूर्ण अधिकार स्थानीय सरकारलाई भएको उल्लेख छ भने स्थानीय सरकार सञ्चालन ऐन, २०७४ को दफा ११ (२) को च मा माथि उल्लेखित विषयलाई थप विस्तार गरिएको छ ।</p>

<p>तसर्थ नेपालको संविधान तथा स्थानीय सरकार सञ्चालन ऐन, २०७४ ले प्रदान गरेको अधिकार प्रयोग गरी संघीय मामिला तथा सामान्य प्रशासन मन्त्रालयले तयार पारेको गाउँ/नगर वस्तुगत विवरण तयारी कार्यविधि, २०७५, (संशोधन २०७९) अनुरुप स्थानीय स्तरका विकासको योजना निर्माण, नीतिनिर्माण तथा स्थानीय सूचनाको प्रमुख श्रोतको रुपमा रहने यो वस्तुगत विवरणले लिखु पिके गाउँपालिकालाई विकास र समृद्धिको समुचित दिशातर्फ उन्मुख हुन सहयोग गर्ने विश्वासका साथ यो प्रतिवेदन तयार भएको छ ।</p>""",
                "summary_nepali": "संघीय शासन प्रणाली र स्थानीय तहको अधिकारका सन्दर्भमा लिखु पिके गाउँपालिकाको वस्तुगत विवरण तयारीको पृष्ठभूमि",
                "order": 1,
            },
            {
                "section_number": "१.२",
                "title": "Objectives",
                "title_nepali": "उद्देश्य",
                "slug": "objectives",
                "content_nepali": """<p>पाश्र्वचित्र निर्माणको प्रमुख उद्देश्य भनेकै लिखु पिके गाउँपालिकाको समग्र वस्तुगत अवस्थाको जानकारीहरूलाई सुव्यवस्थित ढङ्गले अभिलेखीकरण गर्ने र ती तथ्याङ्क र सूचनाहरूलाई अद्यावधिक गर्दै आवश्यक पर्दा सरोकारवालाहरूलाई सूचना उपलब्ध गराउनु हो । पाश्र्वचित्रका अन्य विशिष्ट उद्देश्यहरू निम्नानुसार रहेका छन्ः–</p>

<p><strong>क)</strong> लिखु पिके गाउँपालिकाको समग्र भौतिक पूर्वाधार, आर्थिक पक्ष, सामाजिक पक्ष, प्राकृतिक सम्पदा तथा विपद्व्यवस्थापन सम्बद्ध पक्षहरूको सूचना तथा तथ्याङ्कको अभिलेख तयार पार्ने ।</p>

<p><strong>ख)</strong> लिखु पिके गाउँपालिकाको सेवाप्रवाह तथा संस्थागत संयन्त्रहरू बारेका सूचना तथा तथ्याङ्कहरूको अभिलेख तयार गर्ने ।</p>

<p><strong>ग)</strong> लिखु पिके गाउँपालिकाका सबल पक्षहरू, दुर्बल पक्षहरू, अवसरहरू, चुनौतीहरू तथा सम्भावनाहरूको विश्लेषण गर्ने ।</p>

<p><strong>घ)</strong> लिखु पिके गाउँपालिकाको विभिन्न विषयगत आधार नक्सा तयार गर्ने ।</p>

<p><strong>ङ)</strong> लिखु पिके गाउँपालिकाको समग्र जनसांख्यिक, आर्थिक, सामाजिक, भौतिक, प्राकृतिक, ऐतिहासिक, धार्मिक, साँस्कृतिक तथ्याङ्कहरूको व्याख्या र विश्लेषण गर्ने ।</p>

<p><strong>च)</strong> प्राप्त सूचनाहरूको वर्गीकरण गरी सुव्यवस्थित र सरल ढंगले सर्वसाधारणले बुझ्न सक्ने गरी विभिन्न खण्डमा विभाजन गरी प्रस्तुत गर्ने ।</p>

<p><strong>छ)</strong> माथि उल्लेखित सम्पुर्ण विषयसँग सम्बन्धित एकमुष्ठ तथ्याङ्कीय आधार तयार पार्ने ।</p>""",
                "summary_nepali": "लिखु पिके गाउँपालिकाको पाश्र्वचित्र निर्माणका मुख्य र विशिष्ट उद्देश्यहरू",
                "order": 2,
            },
            {
                "section_number": "१.३",
                "title": "Legal and Policy Framework",
                "title_nepali": "कानूनी तथा नीतिगत आधारहरू",
                "slug": "legal-policy-framework",
                "content_nepali": """<p>पृष्ठभूमिमा उल्लेख भएजस्तै लिखु पिके गाउँपालिकाको वस्तुगत विवरण तयारीका निम्न आधारहरू रहेका छन्।</p>

<h3>(क) वैधानिक आधार</h3>
<p>नेपालको संविधानको अनुसूची ८ र ९ लाई व्याख्या गर्न बनेको स्थानीय सरकार सञ्चालन ऐन, २०७४ ले स्थानीय तथ्याङ्कहरूको अभिलेख तयार गरी अद्यावधिक गर्ने अधिकार र जिम्मेवारी स्थानीय तहलाई नै प्रदान गरेकोले लिखु पिके गाउँपालिकालाई पाश्र्वचित्र तयार पार्ने आधार बनेको छ ।</p>

<h3>(ख) नीतिगत आधारहरू</h3>
<p>नीतिगत आधारहरू अन्तर्गत नेपाल सरकारले तयार पारेको समग्र योजनाहरू, नीतिहरू, प्रादेशिक नीतिहरू र यी नीतिहरूका आधारमा तयार भएका स्थानीय तहका नीतिहरूलाई कार्यान्वयन गर्न आधारभूत रुपमा आवश्यक तथ्याङ्कहरूको अनिवार्यता हुने भएकाले लिखु पिके गाउँपालिकाको समग्र सूचनाहरू तयार पार्नुपर्ने नीतिगत आवश्यकता रहेको र सूचना व्यवस्थापनको नीतिगत व्यवस्था समेत रहेकाले सोका आधारमा यो वस्तुगत विवरण तयार पारिएको हो ।</p>

<h3>(ग) स्थानीय आवश्यकता</h3>
<p>स्थानीय सरकार सञ्चालन गर्न तथा स्थानीय आवश्यकताहरूको पहिचान गर्न वस्तुगत सूचनाहरूको आवश्यकता पर्दछ । स्थानीय आवश्यकताहरूको पहिचान पश्चात् विकास निर्माण नीति, योजना तथा कार्यक्रमहरू तय गर्न सकिन्छ । तसर्थ समग्र विकास प्रक्रियालाई अगाडि बढाउँदै स्थानीय सरकार सञ्चालन गर्न आवश्यक सूचना तथा तथ्याङ्कहरूको संगालोको टड्कारो आवश्यकता रहने हुँदा यो नै वस्तुगत विवरण तयारीको अर्को महत्वपूर्ण आधार हो ।</p>

<p>यी बाहेक नेपालले पक्षराष्ट्र भई हस्ताक्षर गरेका अन्तराष्ट्रिय सन्धी तथा सम्झौताहरूलाई कार्यान्वयन गर्न समेत वस्तुगत सूचनाहरूको आवश्यकता पर्दछ । दिगो विकास लक्ष्य हासल गर्न जलवायु परिवर्तनका असरहरू न्यूनीकरण गर्न, मानवअधिकारको सुनिश्चितता गर्न, पर्यावरणीय सन्तुलन कायम गरी दिगो विकास गर्न तथ्यपरक सूचनाहरूको आवश्यकता पर्ने भएकाले यी आवश्यकताका आधारमा यो विवरण तयार पारिएको हो ।</p>""",
                "summary_nepali": "लिखु पिके गाउँपालिकाको वस्तुगत विवरण तयारीका वैधानिक, नीतिगत र स्थानीय आधारहरू",
                "order": 3,
            },
            {
                "section_number": "१.४",
                "title": "Preparation Phases",
                "title_nepali": "तयारीका चरणहरू",
                "slug": "preparation-phases",
                "content_nepali": """<p>यस लिखु पिके गाउँपालिकाको पाश्र्वचित्रको तयारी गर्दा प्रयोग गरिएका विधिहरू निम्नानुसार छन्—</p>

<p>✓ विशिष्टीकृत प्रश्नावली निर्माण गरी एन्ड्रोइड एप्स (KoBo Collect) द्वारा प्रत्येक घरपरिवारको जनसांख्यिक, आर्थिक, सामाजिक र भौतिक पक्षहरूको विवरण संकलन गर्न गणकहरू परिचालन गरी आवश्यक तथ्याङ्क संकलन गरिएको ।</p>

<p>✓ यसमा लिखु पिके गाउँपालिकाको विभिन्न विषयगत शाखा, विषयगत कार्यालय तथा विभिन्न संघसंस्थाहरूबाट उपलब्ध तथ्याङ्कहरू समावेश गरिएको।</p>

<p>✓ सबै वडाका अध्यक्ष तथा अन्य पदाधिकारीसँग प्रत्यक्ष अन्तर्वार्ता विधि प्रयोग गरी तथ्याङ्क संकलन गरिएको ।</p>

<p>✓ घरधुरी तथाङ्क संकलन २०८१, र अन्य विभिन्न सर्वेक्षण आदिका नतिजाहरू समावेश गरिएको।</p>

<p>✓ यस अध्ययन प्रतिवेदनमा तथ्याङ्कको विश्लेषणका क्रममा विभिन्न तालिकाहरू, चित्रहरू तथा नक्साको प्रयोग गरी वर्णनात्मक तथा तुलनात्मक रुपमा विश्लेषण गरिएको।</p>

<p>पाश्र्वचित्र तयार गर्ने कार्य प्राथमिक (Primary) तथा द्वित्तीय (Secondary) सूचना संकलन पद्दती प्रयोग गरी गरिएको छ । भू–उपयोग, सडकहरू र सोको गुणस्तर तथा वातावरणीय समस्याहरू जस्ता प्राथमिक तथ्याङ्कहरू, भौगोलिक सूचना प्रणाली तथ्याङ्क (GIS Data), स्थलस्वरुप नक्सा, हवाई नक्सा, नापी नक्सा, स्थलगत निरीक्षण तथा अन्तर्वार्ता विधि प्रयोग गरी संकलन गरिएको छ । यसका साथै लिखु पिके गाउँपालिका स्थित विभिन्न सरकारी एवं गैरसरकारी निकायहरूका पदाधिकारीहरू, बुद्धिजीवीहरू उपलब्ध प्रतिष्ठित व्यक्तित्वहरूसँग छलफल एवं अन्तर्वार्ता गरी गाउँपालिकाका प्रमुख समस्या एवं विकासका सम्भावनाहरू बारे जानकारी लिइएको छ । लिखु पिके गाउँपालिकाका समग्र तथ्याङ्कहरू जस्तैः भौतिक, वातावरणीय, सामाजिक, आर्थिक, वित्तीय एवं संस्थागत तथ्याङ्कहरू गाउँपालिका कार्यालय लगायत गाउँपालिका स्थित सरकारी एवं गैरसरकारी कार्यालयहरूको रेकर्डबाट र केही तथ्याङ्कहरू सम्वन्धित विभाग तथा अन्य निकायहरूबाट प्रकाशित प्रतिवेदन एवं पुस्तकहरू अध्ययन गरी संकलन गरिएको छ ।</p>""",
                "summary_nepali": "लिखु पिके गाउँपालिकाको पाश्र्वचित्र तयारीमा प्रयोग गरिएका विधिहरूको परिचय",
                "order": 4,
            },
            {
                "section_number": "१.४.१",
                "title": "Format, Tools and Procedure Preparation",
                "title_nepali": "वस्तुस्थिति विवरण ढाँचा, औजार तथा कार्यविधि तयारी",
                "slug": "format-tools-procedure",
                "content_nepali": """<p>यस तयारीको पहिलो चरणमा देहाय बमोजिम गतिविधिहरु संचालन गरिएका छन्ः–</p>

<p><strong>•</strong> लिखु पिके गाउँपालिका क्षेत्रको भौगोलिक अवस्था, जनसंख्या, सामाजिक, आर्थिक, प्राकृतिक, भौतिक, वातावरणीय र संस्थागत वस्तुस्थिति झल्कने र भौगोलिक तथा सामाजिक रुपमा खण्डीकृत विवरण खुल्ने गरी वस्तुस्थिति विवरण तयारी कार्य प्रारम्भ गर्न कार्यपालिका बैठकबाट निर्णय गरियो।</p>

<p><strong>•</strong> वस्तुस्थिति विवरणको स्तरीय ढाँचा अनुसार घरधुरी सर्वेक्षण, संस्थागत सर्वेक्षण एवं सहभागितामूलक लेखाजोखा सर्वेक्षणका लागि विज्ञहरुको समेत संलग्नतामा प्रश्नावलीलाई अन्तिम रुप दिइयो ।</p>

<p><strong>•</strong> पारिवारिक विवरण संकलनका लागि विद्युतीय माध्यम (Cloud Form) मा आधारित उपयुक्त कम्प्युटर सफ्टवेयर प्रणाली तथा मोबाईल एप्लीकेशन निर्माण गरियो ।</p>""",
                "summary_nepali": "लिखु पिके गाउँपालिकाको वस्तुस्थिति विवरण तयारीको पहिलो चरणमा संचालित गतिविधिहरू",
                "order": 5,
            },
            {
                "section_number": "१.४.२",
                "title": "Preparation Workshop",
                "title_nepali": "वस्तुस्थिति विवरण तयारी कार्यशाला",
                "slug": "preparation-workshop",
                "content_nepali": """<p>वस्तुस्थिति विवरण तयारीको लागि लिखु पिके गाउँपालिकाले कार्यपालिकाका पदाधिकारी, कर्मचारी र सरोकारवालाहरुबीच वस्तुस्थित विवरणको स्तरीय ढाँचा, तथ्याङ्कको स्रोत तथा संकलन एवं विश्लेषण तयारी विधिबारे साझा धारणा, बुझाई र अपनत्व कायम गर्न छलफलबाट कार्ययोजना तयार गर्नका लागि तथा वस्तुस्थिति विवरण तयार गर्ने कार्यको जिम्मेवारी र कार्ययोजना निर्धारण गर्नका लागि गाउँपालिका अध्यक्ष, उप–अध्यक्ष, कार्यपालिकाका सदस्यहरु, प्रमुख प्रशासकीय अधिकृत, वडा सचिवहरु, विषयगत शाखा/उपशाखा/इकाई प्रमुखहरु, गाउँपालिकाबाट छनौट गरिएका स्थानीयस्तरको जानकार विशेषज्ञ वा स्थानीय विज्ञहरुको सहभागितामा एक दिनको वस्तुस्थिति विवरण तयारी कार्यशाला गोष्ठी संचालन गरियो।</p>""",
                "summary_nepali": "लिखु पिके गाउँपालिकामा आयोजित वस्तुस्थिति विवरण तयारी कार्यशालाको विवरण",
                "order": 6,
            },
            {
                "section_number": "१.४.३",
                "title": "Facilitator and Volunteer Selection and Orientation",
                "title_nepali": "सहजकर्ता तथा स्वयंसेवी गणक छनौट अभिमुखीकरण र परिचालन",
                "slug": "facilitator-volunteer-selection",
                "content_nepali": """<p>तयारीको यो तेश्रो चरणमा वडा समिति तथा वडा कार्यालयहरुले लिखु पिके गाउँपालिकाको समन्वयमा गणकहरु छनौट गरी अन्तिम नाम सार्वजनिक गर्नका लागि गाउँपालिकामा पठाउने कार्य भयो । गणकहरूको छनौट प्रक्रियामा निश्चित मापदण्डहरू तय गरिएका थिए भने वडागत आवश्यकताका आधारमा गणकहरूको छनौट गरिएको थियो । यसरी छनौट भएका गणक तथा सहजकर्ताहरूलाई मोबाइल प्रविधिको प्रयोग एवम् प्रश्नावली सम्बन्धी बुझाई तथा सर्वेक्षण विधि, प्रक्रिया आदिका लागि तालिम प्रदान गरियो । यसरी संचालन गरिएको तालिममा प्रयोगात्मक विधिको समेत अभ्यास गरी गणकहरूलाई परिचालनको तयारी गरियो ।</p>""",
                "summary_nepali": "लिखु पिके गाउँपालिकामा सहजकर्ता र गणकहरूको छनौट, तालिम र परिचालनको विवरण",
                "order": 7,
            },
            {
                "section_number": "१.४.४",
                "title": "Data Collection",
                "title_nepali": "तथ्याङ्क संकलन",
                "slug": "data-collection",
                "content_nepali": """<p>लिखु पिके गाउँपालिकाको वस्तुस्थिति विवरण निर्माणका लागि दुई किसिमका तथ्याङ्कहरू संकलन गरिएको थियो । संस्थागत विवरण संकलन तथा घरधुरी सर्वेक्षण । संस्थागत विवरण संकलन अन्तर्गत प्रश्नावलीहरूको माध्यमबाट हरेक वडा कार्यालय तथा गाउँपालिकाको विभिन्न शाखाहरूको समेत सहयोग र समन्वयमा विवरणहरू संकलन गर्ने कार्य गरियो । यसरी संस्थागत विवरणहरू संकलन गर्ने सन्दर्भमा स्रोत नक्सा एवं GIS Mapping लाई व्यवस्थित गर्नका लागि GIS Application लिइएको थियो । यसैगरी घरधुरी सर्वेक्षण अन्तर्गत तालिम प्राप्त गणकहरूले मोबाइल एप्स सहितको प्रविधिको प्रयोग गरी प्रत्येक घरधुरीमा पुगेर GPS Application सहितको तथ्यांक संकलन गर्ने कार्य गरियो । यसरी संकलन गरिएको तथ्यांकहरूलाई सर्भरमा एकत्रित गरी प्रत्येक दिन प्राप्त तथ्यांकहरूलाई केलाएर गुणस्तर निर्धारण सहित आवश्यकता अनुसार गणकहरूलाई पृष्ठपोषण दिने कार्य गरियो ।</p>""",
                "summary_nepali": "लिखु पिके गाउँपालिकामा संस्थागत र घरधुरी सर्वेक्षण मार्फत तथ्याङ्क संकलनको विवरण",
                "order": 8,
            },
            {
                "section_number": "१.४.५",
                "title": "Data Processing and Analysis",
                "title_nepali": "तथ्याङ्क प्रशोधन तथा विश्लेषण र स्रोत नक्सा तयारी",
                "slug": "data-processing-analysis",
                "content_nepali": """<p>पारिवारिक विवरणबाट प्राप्त तथ्यांकलाई व्यवस्थित तथा विश्लेषणका लागि कम्प्युटर सफ्टवेयरको डिजाइन तथा विकास गरी आवश्यकता अनुसारका तालिकाहरू तयार गरिनुका साथै थप विश्लेषणका लागि MS Excel को पनि प्रयोग गरियो भने संस्थागत तथ्यांकहरूलाई MS Excel को प्रयोग गरी विश्लेषण गर्ने कार्य संचालन भयो । स्रोत नक्सा तयारीका लागि पनि दुवै तरिकाहरू जस्तै GIS Database लाई आधार मानी सफ्टवेयरको प्रयोग गरी GIS मा आधारित स्रोत नक्सा बनाउने, तथ्यांक व्यवस्थापनका लागि विकास गरिएको सफ्टवेयरमा पनि GPS Application राखेर Google Map को प्रयोगबाट Mapping गर्ने विधिको प्रयोग गरियो ।</p>""",
                "summary_nepali": "लिखु पिके गाउँपालिकाका तथ्याङ्कको प्रशोधन, विश्लेषण र स्रोत नक्सा तयारीको विवरण",
                "order": 9,
            },
            {
                "section_number": "१.४.६",
                "title": "Draft Report Preparation",
                "title_nepali": "वस्तुस्थिति विवरणको मस्यौदा तयारी",
                "slug": "draft-report-preparation",
                "content_nepali": """<p>तथ्याङ्क प्रशोधन तथा विश्लेषण र स्रोत नक्सा तयारीबाट प्राप्त प्रतिवेदनहरूलाई व्यवस्थित गर्दै तथा वस्तुस्थिति विवरण तयारी कार्यविधि २०७८, ले निर्देश गरे बमोजिम लिखु पिके गाउँपालिकाका प्रमुख प्रशासकीय अधिकृतको नेतृत्वमा साझेदार संस्था लगायत विज्ञहरूद्वारा वस्तुस्थिति विवरणको मस्यौदा प्रतिवेदन तयारी गरी तोकिएको समयावधिमा लिखु पिके गाउँपालिकामा पेश गरियो ।</p>""",
                "summary_nepali": "लिखु पिके गाउँपालिकाको वस्तुस्थिति विवरणको मस्यौदा प्रतिवेदन तयारीको विवरण",
                "order": 10,
            },
            {
                "section_number": "१.४.७",
                "title": "Feedback Collection",
                "title_nepali": "वस्तुस्थिति विवरण सुझाव संकलन",
                "slug": "feedback-collection",
                "content_nepali": """<p>निर्धारित ढाँचामा गाउँ वस्तुस्थिति विवरणको पहिलो मस्यौदा तयार भएपश्चात् वस्तुस्थिति विवरणको मस्यौदामा छलफल गर्न लिखु पिके गाउँपालिकामा एक दिने प्रमाणीकरण कार्यशालाको आयोजना गरियो । प्रमाणीकरण कार्यशालामा प्रस्तुत भएका सूचना तथा विवरणको शुद्धता र तथ्य यकिन गरी सुधारको लागि सुझाव संकलन गर्ने, वस्तुस्थिति विवरणको मस्यौदाले समेट्न नसकेका विषय क्षेत्र वा परिमार्जन गर्नुपर्ने पक्षहरू अध्ययन गरी समावेश गर्न सुझाव आदान प्रदान गर्ने, वस्तुस्थिति विवरणमा समावेश तथ्याङ्क, सूचना तथा विवरणहरूको अन्तरसम्बन्ध र तुलनात्मक पक्षहरू यकिन गर्ने, वस्तुस्थिती विवरण प्रकाशन पश्चात् यसका विवरणहरू योजना तर्जुमा, विकास निर्माण, सेवाप्रवाह, कार्यसम्पादन र नतिजा अनुगमनमा उपयोग गर्ने प्रतिबद्धता जाहेर गर्ने आदि कार्यहरू गरिएको थियो ।</p>""",
                "summary_nepali": "लिखु पिके गाउँपालिकामा आयोजित प्रमाणीकरण कार्यशाला र सुझाव संकलनको विवरण",
                "order": 11,
            },
            {
                "section_number": "१.४.८",
                "title": "Final Report Preparation",
                "title_nepali": "गाउँ वस्तुस्थिति विवरण अन्तिम प्रतिवेदन तयारी",
                "slug": "final-report-preparation",
                "content_nepali": """<p>कार्यशालाबाट प्राप्त भएका सुझावहरूलाई समावेश गरी तथा मस्यौदा प्रतिवेदनमा परिमार्जन गर्नुपर्ने विषयहरु, कार्यशालाबाट प्रस्तुत सुझावहरू बारे सम्बन्धित सरोकारवालासँग आवश्यकतानुसार पुनःपरामर्श गरी एवं वस्तुस्थिति विवरणको स्तरीयता र गुणस्तर सुनिश्चितताका लागि विज्ञहरूका सुझावहरूलाई समेत ध्यान दिई वस्तुस्थिति विवरणलाई अन्तिम रुप दिईएको हो ।</p>""",
                "summary_nepali": "लिखु पिके गाउँपालिकाको वस्तुस्थिति विवरणको अन्तिम प्रतिवेदन तयारीको विवरण",
                "order": 12,
            },
            {
                "section_number": "१.५",
                "title": "Scope of Status Report",
                "title_nepali": "वस्तुस्थिति विवरणको सीमा",
                "slug": "scope-of-report",
                "content_nepali": """<p>राष्ट्रिय योजना आयोग र संघीय मामिला तथा सामान्य प्रशासन मन्त्रालयले निर्धारण गरे बमोजिम लिखु पिके गाउँपालिका पाश्र्वचित्र तयार गर्दा प्रयोग गरिएका तथ्यांकहरूको स्रोत र आधार वर्ष खुलाइएको छ । लिखु पिके गाउँपालिकाका विभिन्न सरकारी तथा गैरसरकारी कार्यालय, अन्य संघसंस्थाले उपलब्ध गराएका तथ्याङ्क, विभिन्न मन्त्रालय, विभागहरू, सम्बन्धित गाउँपालिका आदि स्रोतहरूबाट उपलब्ध तथ्याङ्कको आधारमा यो वस्तुगत विवरण तयार गरिएको छ । पाश्र्वचित्रको अवधारणा अनुसार यसले लिखु पिके गाउँपालिकाको सम्पूर्ण पक्षको यथार्थ जानकारी सरल एवं स्पष्ट रुपमा दिन्छ । अध्ययनलाई यथासक्य वस्तुगत बनाउने प्रयास गरिएको छ । तैपनि स्रोत, साधन तथा सूचना व्यवस्थापनका सिमितताका कारण अपेक्षित सम्पूर्ण सूचनाहरू प्राप्त हुन सकेको छैन । तथापी, अध्ययनमा निर्धारित उद्देश्यका आधारमा आवश्यकता अनुसारका तथ्याङ्क भने समावेश गरिएको छ ।</p>""",
                "summary_nepali": "लिखु पिके गाउँपालिकाको वस्तुस्थिति विवरणको सीमा र स्रोतको विवरण",
                "order": 13,
            },
        ]

        # Create sections
        for section_data in sections_data:
            if force_update:
                # Update or create with force
                section, created = ReportSection.objects.update_or_create(
                    category=category,
                    slug=section_data["slug"],
                    defaults={
                        "title": section_data["title"],
                        "title_nepali": section_data["title_nepali"],
                        "section_number": section_data["section_number"],
                        "content_nepali": section_data["content_nepali"],
                        "summary_nepali": section_data["summary_nepali"],
                        "order": section_data["order"],
                        "is_published": True,
                        "meta_title": f"{section_data['title']} - {category.name}",
                        "meta_description": section_data["summary_nepali"][:200],
                        "meta_keywords": f"लिखु पिके, {section_data['title_nepali']}, वस्तुस्थिति विवरण",
                    },
                )

                if created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Created section: {section.section_number} - {section.title_nepali}"
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Updated section: {section.section_number} - {section.title_nepali}"
                        )
                    )
            else:
                # Only create if doesn't exist
                section, created = ReportSection.objects.get_or_create(
                    category=category,
                    slug=section_data["slug"],
                    defaults={
                        "title": section_data["title"],
                        "title_nepali": section_data["title_nepali"],
                        "section_number": section_data["section_number"],
                        "content_nepali": section_data["content_nepali"],
                        "summary_nepali": section_data["summary_nepali"],
                        "order": section_data["order"],
                        "is_published": True,
                        "meta_title": f"{section_data['title']} - {category.name}",
                        "meta_description": section_data["summary_nepali"][:200],
                        "meta_keywords": f"लिखु पिके, {section_data['title_nepali']}, वस्तुस्थिति विवरण",
                    },
                )

                if created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Created section: {section.section_number} - {section.title_nepali}"
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            f"Section already exists: {section.section_number} - {section.title_nepali}"
                        )
                    )

        self.stdout.write(
            self.style.SUCCESS("Successfully populated Introduction chapter content!")
        )
        self.stdout.write(
            self.style.SUCCESS(f"Category: {category.name} ({category.name_nepali})")
        )
        self.stdout.write(
            self.style.SUCCESS(f"Total Sections: {category.sections.count()}")
        )
