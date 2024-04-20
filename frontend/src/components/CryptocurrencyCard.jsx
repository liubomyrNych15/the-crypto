import { Card } from 'antd';

function CryptocurrencyCard(props) {
    const { currency } = props;

    const price = Math.round(currency.quote.USD.price);

    if (!currency)
        return null;

    return (
        <div>
            <Card
                title={
                    <div className="flex items-center gap-3">
                        <img src={`https://s2.coinmarketcap.com/static/img/coins/64x64/${currency.id}.png`}/>
                        <span>{currency.name}</span>
                    </div>
                }
                style={{
                    width: 300,
                }}
            >
                <p>Current price: {price}</p>
                <p>Price change in 24 hours: {currency.quote.USD.percent_change_24h}</p>
                <p>Current capitalization: {currency.quote.USD.market_cap}</p>
            </Card>
        </div>
    );
}

export default CryptocurrencyCard;
